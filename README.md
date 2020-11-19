# json-to-string-recursive


A python script to exract recursively path strings into a file


for example -

  json:

  {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "image":[
      {
        "url": "images/0001.jpg",
        "width": 200,
        "height": 200
      },
      {
        "url": "images/00032.jpg",
        "width": 1200,
        "height": 12300
      }
    ],
    "thumbnail":
      {
        "url": "images/thumbnails/0001.jpg",
        "width": 32,
        "height": 32
      }
  }
  
  output:
  
  id.0001
  type.donut
  name.Cake
  image.url.images/0001.jpg
  image.width.200
  image.height.200
  image.url.images/00032.jpg
  image.width.1200
  image.height.12300

  thumbnail.url.images/thumbnails/0001.jpg
  thumbnail.width.32
  thumbnail.height.32
