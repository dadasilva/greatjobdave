---
layout: post
title: "Photo Gallery Post Template"
date: 2024-04-11
categories: [templates, photos]
style: photo
images:
  - url: "/assets/images/photo1.jpg"
    caption: "First photo description"
  - url: "/assets/images/photo2.jpg"
    caption: "Second photo description"
  - url: "/assets/images/photo3.jpg"
    caption: "Third photo description"
---

# Photo Gallery Post

A brief introduction to your photo collection. Explain the context or story behind these images.

## The Gallery

{% for image in page.images %}
![{{ image.caption }}]({{ image.url }})
*{{ image.caption }}*

{% endfor %}

## Technical Details

- Camera: [Your Camera Model]
- Lens: [Lens Details]
- Settings: [Camera Settings]

## Location

Where these photos were taken and any relevant details about the location or conditions. 