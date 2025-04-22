---
layout: default
title: greatjobdave.net
---

<!-- HEADER  -->
<header class="sticky-top">
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-3 ps-4">
        <h1 class="site-title mb-0">
          greatjobdave<span class="text-muted">.net</span>
        </h1>
      </div>
    </div>
  </div>
</header>

<!-- MAIN CONTENT -->
<div class="container-fluid mt-5">
  <div class="row">
    <!-- SIDEBAR -->
    <div class="col-md-3 sidebar-container ps-4">
      <aside class="archive-sidebar">
        <!-- Style Switcher -->
        <div class="style-switcher mb-4">
          <h3 class="sidebar-title">
            <i class="fas fa-palette mr-2"></i>Work
          </h3>
          <div class="style-options">
            <button class="style-option active" data-style="all">
              <i class="fas fa-border-all"></i> All
            </button>
            <button class="style-option" data-style="standard">
              <i class="fas fa-file-alt"></i> Standard
            </button>
            <button class="style-option" data-style="photo">
              <i class="fas fa-camera"></i> Photo
            </button>
            <button class="style-option" data-style="code">
              <i class="fas fa-code"></i> Code
            </button>
            <button class="style-option" data-style="audio">
              <i class="fas fa-music"></i> Audio
            </button>
            <button class="style-option" data-style="model">
              <i class="fas fa-cube"></i> 3D Model
            </button>
          </div>
        </div>

        <!-- Archive -->
        <h3 class="sidebar-title">
          <i class="fas fa-calendar-alt mr-2"></i>Archive
        </h3>
        {% assign postsByYear = site.posts | group_by_exp:"post", "post.date | date: '%Y'" %}
        <div class="accordion" id="archiveAccordion">
          {% for year in postsByYear %}
            <div class="year-group">
              <h4 class="year-title">
                <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#year{{ year.name }}" aria-expanded="true">
                  <i class="fas fa-chevron-right year-icon"></i>
                  {{ year.name }}
                </button>
              </h4>
              <div id="year{{ year.name }}" class="collapse" data-parent="#archiveAccordion">
                {% assign postsByMonth = year.items | group_by_exp:"post", "post.date | date: '%B'" %}
                {% for month in postsByMonth %}
                  <div class="month-group">
                    <h5 class="month-title">
                      <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#month{{ year.name }}{{ month.name }}" aria-expanded="false">
                        <i class="fas fa-chevron-right month-icon"></i>
                        {{ month.name }}
                      </button>
                    </h5>
                    <div id="month{{ year.name }}{{ month.name }}" class="collapse">
                      <ul class="day-list">
                        {% for post in month.items %}
                          <li class="day-item">
                            <span class="day-date">{{ post.date | date: "%-d" }}</span>
                            <a href="#" class="day-link" data-toggle="collapse" data-target="#post-{{ post.title | slugify }}" aria-expanded="false">{{ post.title }}</a>
                          </li>
                        {% endfor %}
                      </ul>
                    </div>
                  </div>
                {% endfor %}
              </div>
            </div>
          {% endfor %}
        </div>
      </aside>
    </div>

    <!-- BLOG POSTS -->
    <div class="col-md-9 posts-container">
      <section class="blog-posts">
          {% assign published_posts = site.posts | where_exp: "post", "post.draft != true" %}
          {% if published_posts.size == 0 %}
            <div class="no-posts">
              <h2><span>🦗</span><span>🦗</span><span>🦗</span></h2>
              <p>No published posts yet! Check back soon for updates.</p>
            </div>
          {% else %}
            <div class="row">
              {% for post in published_posts %}
              <div class="col-md-4 mb-5 post-card" data-post-id="post-{{ post.title | slugify }}" data-style="{{ post.style }}">
                <article class="card">
                  {% if post.style == "audio" and post.audio_url %}
                    <div class="card-audio-wrapper">
                      <div class="audio-player">
                        <audio controls>
                          <source src="{{ post.audio_url }}" type="audio/mpeg">
                          Your browser does not support the audio element.
                        </audio>
                        <div class="audio-waveform" data-audio="{{ post.audio_url }}"></div>
                      </div>
                    </div>
                  {% elsif post.style == "model" and post.model_url %}
                    <div class="card-model-wrapper">
                      <div class="model-viewer" data-model="{{ post.model_url }}">
                        <div class="model-placeholder">
                          <i class="fas fa-cube"></i>
                          <span>Click to view 3D model</span>
                        </div>
                      </div>
                    </div>
                  {% elsif post.style == "code" %}
                    <div class="card-code-wrapper">
                      <div class="code-preview">
                        <i class="fas fa-code"></i>
                      </div>
                    </div>
                  {% elsif post.image %}
                    <div class="card-img-wrapper">
                      <img src="{{ post.image | relative_url }}" class="card-img-top" alt="{{ post.title }}">
                      <div class="image-overlay lightbox-trigger" data-image="{{ post.image | relative_url }}">
                        <i class="fas fa-search-plus"></i>
                      </div>
                    </div>
                  {% else %}
                    <div class="card-standard-wrapper">
                      <div class="standard-preview">
                        <i class="fas fa-file-alt"></i>
                      </div>
                    </div>
                  {% endif %}
                  <div class="card-body d-flex flex-column">
                    <h2 class="card-title h3">
                      <a href="#" data-toggle="collapse" data-target="#post-{{ post.title | slugify }}" aria-expanded="false">{{ post.title }}</a>
                    </h2>
                    <div class="card-text">
                      <p class="text-muted mb-2">
                        <i class="far fa-calendar-alt"></i> {{ post.date | date: "%b %-d, %Y" }}
                        {% if post.categories %}
                          <span class="ml-3">
                            <i class="fas fa-tags"></i> {{ post.categories | join: ", " }}
                          </span>
                        {% endif %}
                      </p>
                      <p>{{ post.excerpt | strip_html | truncatewords: 25 }}</p>
                    </div>
                    <button class="btn btn-primary" data-toggle="collapse" data-target="#post-{{ post.title | slugify }}" aria-expanded="false">
                      Read More <i class="fas fa-arrow-right ml-2"></i>
                    </button>
                  </div>
                </article>
              </div>
              {% endfor %}
            </div>

            <div class="no-matching-posts" style="display: none;">
              <h2><span>🔍</span></h2>
              <p>No posts found for this category. Try selecting different work!</p>
            </div>
          {% endif %}

        <!-- Expanded Posts Container -->
        <div class="expanded-posts-container">
          {% for post in site.posts %}
          <div class="collapse expanded-post-wrapper" id="post-{{ post.title | slugify }}" data-style="{{ post.style }}">
            <div class="expanded-post">
              <button class="btn btn-outline-primary close-post" data-toggle="collapse" data-target="#post-{{ post.title | slugify }}" aria-expanded="true">
                <i class="fas fa-times"></i>
              </button>
              <div class="expanded-post-header">
                <h2>{{ post.title }}</h2>
                <p class="text-muted">
                  <i class="far fa-calendar-alt"></i> {{ post.date | date: "%b %-d, %Y" }}
                  {% if post.categories %}
                    <span class="ml-3">
                      <i class="fas fa-tags"></i> {{ post.categories | join: ", " }}
                    </span>
                  {% endif %}
                </p>
              </div>
              {% if post.style == "photo" %}
                <div class="photo-gallery">
                  {% if post.image %}
                    <div class="expanded-post-image lightbox-trigger" data-image="{{ post.image | relative_url }}">
                      <img src="{{ post.image | relative_url }}" alt="{{ post.title }}">
                      <div class="image-overlay">
                        <i class="fas fa-search-plus"></i>
                      </div>
                    </div>
                  {% endif %}
                  {{ post.content }}
                  {% if post.gallery %}
                    <div class="gallery-grid">
                      {% for image in post.gallery %}
                        <div class="gallery-item">
                          <div class="gallery-image lightbox-trigger" data-image="{{ image.url | relative_url }}">
                            <img src="{{ image.url | relative_url }}" alt="{{ image.description }}">
                            <div class="image-overlay">
                              <i class="fas fa-search-plus"></i>
                            </div>
                          </div>
                          {% if image.description %}
                            <p class="gallery-description">{{ image.description }}</p>
                          {% endif %}
                        </div>
                      {% endfor %}
                    </div>
                  {% endif %}
                </div>
              {% elsif post.style == "audio" and post.audio_url %}
                <div class="expanded-audio-player">
                  <audio controls>
                    <source src="{{ post.audio_url }}" type="audio/mpeg">
                    Your browser does not support the audio element.
                  </audio>
                  <div class="audio-waveform" data-audio="{{ post.audio_url }}"></div>
                </div>
              {% elsif post.style == "model" and post.model_url %}
                <div class="expanded-model-viewer" data-model="{{ post.model_url }}">
                  <div class="model-placeholder">
                    <i class="fas fa-cube"></i>
                    <span>Loading 3D model...</span>
                  </div>
                </div>
              {% elsif post.image %}
                <div class="expanded-post-image lightbox-trigger" data-image="{{ post.image | relative_url }}">
                  <img src="{{ post.image | relative_url }}" alt="{{ post.title }}">
                  <div class="image-overlay">
                    <i class="fas fa-search-plus"></i>
                  </div>
                </div>
              {% endif %}
              <div class="expanded-post-content">
                {% if post.style != "photo" %}
                  {{ post.content }}
                {% endif %}
              </div>
            </div>
          </div>
          {% endfor %}
        </div>
      </section>
    </div>
  </div>
</div>

<!-- Theme Toggle Button -->
<button class="theme-toggle" data-theme="light">
  <i class="fas fa-sun"></i>
  <i class="fas fa-moon"></i>
</button>

<!-- Lightbox -->
<div class="lightbox">
  <button class="lightbox-close">
    <i class="fas fa-times"></i>
  </button>
  <img src="" alt="" class="lightbox-image">
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  // Get all collapse elements
  const collapseElements = document.querySelectorAll('.expanded-post-wrapper');
  const postGrid = document.querySelector('.post-grid');
  const sidebar = document.querySelector('.sidebar-container');
  
  // Add event listeners for bootstrap collapse events
  collapseElements.forEach(function(element) {
    element.addEventListener('show.bs.collapse', function() {
      // Add fade class to post grid instead of hiding it
      postGrid.style.opacity = '0.2';
      postGrid.style.pointerEvents = 'none';
      sidebar.style.opacity = '0.2';
      sidebar.style.pointerEvents = 'none';
      document.body.style.overflow = 'hidden';
    });
    
    element.addEventListener('hidden.bs.collapse', function() {
      // Restore post grid visibility
      postGrid.style.opacity = '';
      postGrid.style.pointerEvents = '';
      sidebar.style.opacity = '';
      sidebar.style.pointerEvents = '';
      document.body.style.overflow = '';
    });
  });

  // Lightbox functionality
  const lightbox = document.querySelector('.lightbox');
  const lightboxImage = lightbox.querySelector('.lightbox-image');
  const lightboxClose = lightbox.querySelector('.lightbox-close');
  const lightboxTriggers = document.querySelectorAll('.lightbox-trigger');

  function openLightbox(imageSrc) {
    lightboxImage.src = imageSrc;
    lightbox.classList.add('show');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    lightbox.classList.remove('show');
    document.body.style.overflow = '';
    setTimeout(() => {
      lightboxImage.src = '';
    }, 300);
  }

  lightboxTriggers.forEach(trigger => {
    trigger.addEventListener('click', () => {
      const imageSrc = trigger.dataset.image;
      openLightbox(imageSrc);
    });
  });

  lightboxClose.addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) {
      closeLightbox();
    }
  });

  // Close lightbox with escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && lightbox.classList.contains('show')) {
      closeLightbox();
    }
  });

  // Theme switching functionality
  const themeToggle = document.querySelector('.theme-toggle');
  let userThemePreference = localStorage.getItem('theme');
  let isAutoTheme = localStorage.getItem('autoTheme') !== 'false';

  function setTheme(isDark, updateStorage = true) {
    document.documentElement.setAttribute('data-theme', isDark ? 'dark' : 'light');
    themeToggle.setAttribute('data-theme', isDark ? 'dark' : 'light');
    if (updateStorage) {
      localStorage.setItem('theme', isDark ? 'dark' : 'light');
      localStorage.setItem('autoTheme', 'false');
      isAutoTheme = false;
    }
  }

  function checkTime() {
    if (!isAutoTheme) return;
    const hour = new Date().getHours();
    // Dark mode between 6 PM (18:00) and 6 AM (6:00)
    const isDark = hour >= 18 || hour < 6;
    setTheme(isDark, false);
  }

  // Initialize theme
  if (userThemePreference) {
    setTheme(userThemePreference === 'dark', false);
  } else {
    checkTime();
  }

  // Theme toggle click handler
  themeToggle.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    setTheme(currentTheme === 'light');
  });

  // Check every minute for theme changes (only if auto theme is enabled)
  setInterval(checkTime, 60000);

  // Check when the tab becomes visible again
  document.addEventListener('visibilitychange', function() {
    if (!document.hidden && isAutoTheme) {
      checkTime();
    }
  });

  // Style switcher functionality
  const styleButtons = document.querySelectorAll('.style-option');
  const postCards = document.querySelectorAll('.post-card');
  const noMatchingPosts = document.querySelector('.no-matching-posts');

  styleButtons.forEach(button => {
    button.addEventListener('click', () => {
      // Update active button
      styleButtons.forEach(btn => btn.classList.remove('active'));
      button.classList.add('active');

      const selectedStyle = button.dataset.style;
      let visiblePosts = 0;

      // Filter posts
      postCards.forEach(card => {
        const postStyle = card.dataset.style;
        if (selectedStyle === 'all' || postStyle === selectedStyle) {
          card.style.display = '';
          setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          }, 50);
          visiblePosts++;
        } else {
          card.style.opacity = '0';
          card.style.transform = 'translateY(20px)';
          setTimeout(() => {
            card.style.display = 'none';
          }, 300);
        }
      });

      // Show/hide no matching posts message
      if (visiblePosts === 0) {
        setTimeout(() => {
          noMatchingPosts.style.display = 'block';
          noMatchingPosts.style.opacity = '1';
          noMatchingPosts.style.transform = 'translateY(0)';
        }, 350);
      } else {
        noMatchingPosts.style.opacity = '0';
        noMatchingPosts.style.transform = 'translateY(20px)';
        setTimeout(() => {
          noMatchingPosts.style.display = 'none';
        }, 300);
      }
    });
  });
});
</script> 