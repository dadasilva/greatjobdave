---
layout: post
title: Audio Post Template
style: audio
draft: true
soundcloud_id: YOUR_SOUNDCLOUD_ID
spotify_id: YOUR_SPOTIFY_ID
categories: [music, audio]
image: YOUR_ALBUM_COVER_URL
preview: "Write a brief, compelling description of the track here. This will appear in the preview section and card view."
---

<div class="preview-section">
  <div class="album-info">
    <img src="{{ page.image }}" alt="{{ page.title }} album cover" class="album-cover">
    <div class="track-details">
      <h2>{{ page.title }}</h2>
      <p class="artist">Artist Name</p>
      <p class="album">From the album "Album Name" (Year)</p>
      <p class="duration">Track Duration</p>
      <p class="description">{{ page.preview }}</p>
    </div>
  </div>
</div>

<div class="audio-embed soundcloud-embed">
  <iframe width="100%" 
          height="166" 
          scrolling="no" 
          frameborder="no" 
          allow="autoplay" 
          src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/{{ page.soundcloud_id }}&color=%2390B597&auto_play=false&hide_related=true&show_comments=true&show_user=true&show_reposts=false&show_teaser=false">
  </iframe>
</div>

## About the Track

Write about the track here. Some suggestions:
- Musical elements and composition
- Historical context
- Personnel and instruments
- Recording details
- Impact and legacy

## Credits

List credits here:
- Composer(s):
- Performer(s):
- Producer(s):
- Recording Studio:
- Release Date:

## Additional Notes

Any other relevant information about the track, such as:
- Awards and recognition
- Interesting facts
- Related works
- Cultural impact

<!--
TEMPLATE INSTRUCTIONS:

1. Set draft: false when ready to publish
2. Fill in all metadata in the front matter:
   - title: The title of your post
   - soundcloud_id: The ID from your SoundCloud track URL
   - spotify_id: The ID from your Spotify track URL
   - image: URL to the album cover
   - preview: A brief description (1-2 sentences)
   - categories: Relevant categories for the post

3. Replace placeholder content in each section
4. Remove these instructions before publishing
--> 