import os
from .models import Jobs,JobDetail
from .serializers import JobSerializer,JobDetailSerializer
from bs4 import BeautifulSoup
import requests
from rest_framework import viewsets

# Create your views here.
# base_url='https://www.brightermonday.co.ke'
url = 'https://www.brightermonday.co.ke/jobs'
page = requests.get(url)

if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'html.parser')
    wens = soup.find_all('div', class_='flex-1 flex items-center justify-between px-5 py-3 rounded-tr-md w-full pr-5 rounded-t1-md px-5')
    
    for wen in wens:
        # div = soup.find('div', class_='mr-6 flex-shrink-0')
        jobss = Jobs()
        jobss.link = wen.find('a',class_='relative mb-3 text-lg font-medium break-words focus:outline-none metrics-apply-now text-link-500 text-loading-animate')['href']
        jobss.title = wen.find('p').text.strip()
        # jobss.image = div.find('img')['src']
        jobss.save()
        
        jobss.title = wen.find('p').text.strip()      
        job_response = requests.get(jobss.link)
        job_soup = BeautifulSoup(job_response.content, 'html.parser')
        summary=job_soup.find('div',class_='py-5 px-4 border-b border-gray-300 md:p-5')
        if summary.find('h3').get_text():
            det=JobDetail()
            det.job=jobss
            det.details=summary.find('h3').get_text()
            det.save()
        if summary.find('p').get_text():
            det=JobDetail()
            det.job=jobss
            det.details=summary.find('p').get_text()
            det.save()
        qualification = summary.find('ul')
        if qualification:
            # qualifications = []
            qualifications_elements = qualification.find_all('li')
            for qual_element in qualifications_elements:
                 det = JobDetail()
                 det.job = jobss
                 det.details=qual_element.get_text()
                 det.save()
                
        descrip = job_soup.find('div', class_='text-sm text-gray-500')
        paragraphs=descrip.find_all('p')
        for paragraph in paragraphs:
            bold_tag =paragraph.find_all('b')
            content=paragraph.get_text()     
            if bold_tag:
                job_detail = JobDetail(job=jobss, details=content,bold=True)
            else:
                job_detail = JobDetail(job=jobss, details=content,bold=False)                
            job_detail.save()
            
            next_sibling = paragraph.find_next_sibling()
                
            if next_sibling and next_sibling.name == 'ul':
                ul_tag = paragraph.find_next_sibling('ul')
                if ul_tag:
                    cont1 = ''
                    for li in ul_tag.find_all('li'):
                        cont1 = li.text.strip()
                        # content+=cont1
                        # content += ' :   ' + cont1
                        content = cont1
                        job_detail1 = JobDetail(job=jobss, details=content,)
                        job_detail1.save()
            
   


class JobViewSet(viewsets.ModelViewSet):
    queryset=Jobs.objects.all()
    serializer_class=JobSerializer
class JobDetailViewSet(viewsets.ModelViewSet):
    queryset=JobDetail.objects.all()
    serializer_class=JobDetailSerializer


