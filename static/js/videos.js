// videos.js - extracted from videos.html
            // Video page functionality
            document.addEventListener('DOMContentLoaded', function() {
                const uploadVideoBtn = document.getElementById('uploadVideoBtn');
                const uploadVideoModal = document.getElementById('uploadVideoModal');
                const closeUploadBtn = document.getElementById('closeUpload');
                const cancelUploadBtn = document.getElementById('cancelUploadBtn');
                const saveUploadBtn = document.getElementById('saveUploadBtn');
                const fileDropArea = document.getElementById('fileDropArea');
                const videoFileInput = document.getElementById('videoFile');
                const videoPlayerModal = document.getElementById('videoPlayerModal');
                const closePlayerBtn = document.getElementById('closePlayer');
                const playerTitle = document.getElementById('playerTitle');
                const playerDescription = document.getElementById('playerDescription');
                const categoryButtons = document.querySelectorAll('.category-btn');
                const videoCards = document.querySelectorAll('.video-card');
                const videoThumbnails = document.querySelectorAll('.video-thumbnail');
                const videoTitles = document.querySelectorAll('.video-title');
                const shareButtons = document.querySelectorAll('.share-btn');
                
                // Open upload modal
                uploadVideoBtn.addEventListener('click', function() {
                    uploadVideoModal.style.display = 'flex';
                });
                
                // Close upload modal functions
                function closeUploadModal() {
                    uploadVideoModal.style.display = 'none';
                    // Reset form
                    document.getElementById('videoTitle').value = '';
                    document.getElementById('videoCategory').value = '';
                    document.getElementById('videoDescription').value = '';
                }
                
                closeUploadBtn.addEventListener('click', closeUploadModal);
                cancelUploadBtn.addEventListener('click', closeUploadModal);
                
                // Close upload modal when clicking outside
                uploadVideoModal.addEventListener('click', function(e) {
                    if (e.target === uploadVideoModal) {
                        closeUploadModal();
                    }
                });
                
                // File drag and drop functionality
                fileDropArea.addEventListener('dragover', function(e) {
                    e.preventDefault();
                    this.classList.add('dragover');
                });
                
                fileDropArea.addEventListener('dragleave', function() {
                    this.classList.remove('dragover');
                });
                
                fileDropArea.addEventListener('drop', function(e) {
                    e.preventDefault();
                    this.classList.remove('dragover');
                    
                    if (e.dataTransfer.files.length) {
                        const file = e.dataTransfer.files[0];
                        if (file.type.startsWith('video/')) {
                            videoFileInput.files = e.dataTransfer.files;
                            // Update UI to show file selected
                            const fileName = file.name;
                            this.innerHTML = `
                                <i class="fas fa-check-circle" style="color: var(--success);"></i>
                                <p>File selected: ${fileName}</p>
                                <input type="file" id="videoFile" class="file-input" accept="video/*">
                            `;
                            // Re-add event listeners
                            document.getElementById('videoFile').addEventListener('change', handleFileSelect);
                            setupFileDropArea();
                        } else {
                            alert('Please select a video file!');
                        }
                    }
                });
                
                // File selection via click
                function handleFileSelect(e) {
                    if (e.target.files.length) {
                        const file = e.target.files[0];
                        const fileName = file.name;
                        fileDropArea.innerHTML = `
                            <i class="fas fa-check-circle" style="color: var(--success);"></i>
                            <p>File selected: ${fileName}</p>
                            <input type="file" id="videoFile" class="file-input" accept="video/*">
                        `;
                        document.getElementById('videoFile').addEventListener('change', handleFileSelect);
                        setupFileDropArea();
                    }
                }
                
                videoFileInput.addEventListener('change', handleFileSelect);
                
                function setupFileDropArea() {
                    const newFileDropArea = document.getElementById('fileDropArea');
                    newFileDropArea.addEventListener('dragover', function(e) {
                        e.preventDefault();
                        this.classList.add('dragover');
                    });
                    newFileDropArea.addEventListener('dragleave', function() {
                        this.classList.remove('dragover');
                    });
                    newFileDropArea.addEventListener('drop', function(e) {
                        e.preventDefault();
                        this.classList.remove('dragover');
                        if (e.dataTransfer.files.length) {
                            const file = e.dataTransfer.files[0];
                            if (file.type.startsWith('video/')) {
                                document.getElementById('videoFile').files = e.dataTransfer.files;
                                const fileName = file.name;
                                this.innerHTML = `
                                    <i class="fas fa-check-circle" style="color: var(--success);"></i>
                                    <p>File selected: ${fileName}</p>
                                    <input type="file" id="videoFile" class="file-input" accept="video/*">
                                `;
                                document.getElementById('videoFile').addEventListener('change', handleFileSelect);
                                setupFileDropArea();
                            } else {
                                alert('Please select a video file!');
                            }
                        }
                    });
                }
                
                // Save video upload
                saveUploadBtn.addEventListener('click', function() {
                    const title = document.getElementById('videoTitle').value.trim();
                    const category = document.getElementById('videoCategory').value;
                    
                    if (!title || !category) {
                        alert('Please fill in all required fields!');
                        return;
                    }
                    
                    if (!videoFileInput.files.length) {
                        alert('Please select a video file to upload!');
                        return;
                    }
                    
                    // In a real app, this would upload to server
                    alert(`Video uploaded successfully!\nTitle: ${title}\nCategory: ${category}`);
                    closeUploadModal();
                });
                
                // Open video player modal
                function openVideoPlayer(videoId) {
                    // In a real app, you would load the actual video
                    const videoCard = document.querySelector(`[data-video-id="${videoId}"]`).closest('.video-card');
                    const title = videoCard.querySelector('.video-title').textContent;
                    const description = videoCard.querySelector('.video-description').textContent;
                    
                    playerTitle.textContent = title;
                    playerDescription.textContent = description;
                    videoPlayerModal.style.display = 'flex';
                }
                
                // Video thumbnail click
                videoThumbnails.forEach(thumb => {
                    thumb.addEventListener('click', function() {
                        const videoId = this.getAttribute('data-video-id');
                        openVideoPlayer(videoId);
                    });
                });
                
                // Video title click
                videoTitles.forEach(title => {
                    title.addEventListener('click', function() {
                        const videoId = this.getAttribute('data-video-id');
                        openVideoPlayer(videoId);
                    });
                });
                
                // Close video player
                closePlayerBtn.addEventListener('click', function() {
                    videoPlayerModal.style.display = 'none';
                });
                
                videoPlayerModal.addEventListener('click', function(e) {
                    if (e.target === videoPlayerModal) {
                        videoPlayerModal.style.display = 'none';
                    }
                });
                
                // Category filtering
                categoryButtons.forEach(button => {
                    button.addEventListener('click', function() {
                        // Remove active class from all buttons
                        categoryButtons.forEach(btn => btn.classList.remove('active'));
                        // Add active class to clicked button
                        this.classList.add('active');
                        
                        const category = this.getAttribute('data-category');
                        
                        // Filter cards
                        videoCards.forEach(card => {
                            if (category === 'all' || card.getAttribute('data-category') === category) {
                                card.style.display = 'block';
                            } else {
                                card.style.display = 'none';
                            }
                        });
                    });
                });
                
                // Social sharing functionality
                shareButtons.forEach(btn => {
                    btn.addEventListener('click', function() {
                        const platform = this.className.includes('facebook') ? 'Facebook' :
                                       this.className.includes('twitter') ? 'Twitter' :
                                       this.className.includes('instagram') ? 'Instagram' :
                                       this.className.includes('youtube') ? 'YouTube' :
                                       this.className.includes('whatsapp') ? 'WhatsApp' : 'Social Media';
                        
                        const videoCard = this.closest('.video-card');
                        const title = videoCard.querySelector('.video-title').textContent;
                        alert(`Sharing "${title}" to ${platform}!\n\nIn a real app, this would open the ${platform} sharing dialog.`);
                    });
                });
            });
