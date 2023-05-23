from django.contrib import admin
from .models import Jobs

# Register your models here.

admin.site.register(Jobs)




""" # image_url = jobss.image.url
    image_url = div.find('img')['src']

    # Send a GET request to fetch the image data
    response = request s.get(image_url)

    if response.status_code == 200:
        # Get the filename from the URL
        filename = os.path.basename(unquote(image_url))

        # Specify the path where you want to save the image
        save_path = 'C:\\Users\\Wences\\Desktop\\brigther monday\\brigth\\media' + filename

        # Save the image to the specified path
        with open(save_path, 'wb') as file:
            file.write(response.content)

        # Open the saved image file
        with open(save_path, 'rb') as file:
            # Create a new File object from the saved image file
            image_file = File(file, name=filename)

            # Assign the image file to the 'image' field of your model
            jobss.image = image_file

    jobss.save() """