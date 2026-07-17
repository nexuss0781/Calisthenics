// motivation.js - extracted from Motivation.html
            // Motivation page functionality
            document.addEventListener('DOMContentLoaded', function() {
                const addMotivationBtn = document.getElementById('addMotivationBtn');
                const addMotivationModal = document.getElementById('addMotivationModal');
                const closeModalBtn = document.getElementById('closeModal');
                const cancelMotivationBtn = document.getElementById('cancelMotivationBtn');
                const saveMotivationBtn = document.getElementById('saveMotivationBtn');
                const fileUploadArea = document.getElementById('fileUploadArea');
                const mediaFilesInput = document.getElementById('mediaFiles');
                const categoryButtons = document.querySelectorAll('.category-btn');
                const motivationCards = document.querySelectorAll('.motivation-card');
                
                // Open modal
                addMotivationBtn.addEventListener('click', function() {
                    addMotivationModal.style.display = 'flex';
                });
                
                // Close modal functions
                function closeModal() {
                    addMotivationModal.style.display = 'none';
                    // Reset form
                    document.getElementById('motivationType').value = '';
                    document.getElementById('motivationTitle').value = '';
                    document.getElementById('motivationDescription').value = '';
                    document.getElementById('motivationAuthor').value = '';
                    document.getElementById('motivationURL').value = '';
                }
                
                closeModalBtn.addEventListener('click', closeModal);
                cancelMotivationBtn.addEventListener('click', closeModal);
                
                // Close modal when clicking outside
                addMotivationModal.addEventListener('click', function(e) {
                    if (e.target === addMotivationModal) {
                        closeModal();
                    }
                });
                
                // File upload functionality
                fileUploadArea.addEventListener('click', function(e) {
                    if (e.target !== mediaFilesInput) {
                        mediaFilesInput.click();
                    }
                });
                
                mediaFilesInput.addEventListener('change', function() {
                    if (this.files.length > 0) {
                        const fileName = this.files[0].name;
                        fileUploadArea.innerHTML = `
                            <i class="fas fa-check-circle" style="color: var(--success);"></i>
                            <p>File selected: ${fileName}</p>
                            <input type="file" id="mediaFiles" accept="image/*,video/*">
                        `;
                        // Re-add event listener to new input
                        document.getElementById('mediaFiles').addEventListener('change', function() {
                            if (this.files.length > 0) {
                                const newFileName = this.files[0].name;
                                fileUploadArea.innerHTML = `
                                    <i class="fas fa-check-circle" style="color: var(--success);"></i>
                                    <p>File selected: ${newFileName}</p>
                                    <input type="file" id="mediaFiles" accept="image/*,video/*">
                                `;
                                document.getElementById('mediaFiles').addEventListener('change', arguments.callee);
                            }
                        });
                    }
                });
                
                // Save motivation
                saveMotivationBtn.addEventListener('click', function() {
                    const type = document.getElementById('motivationType').value;
                    const title = document.getElementById('motivationTitle').value.trim();
                    
                    if (!type || !title) {
                        alert('Please select content type and enter a title!');
                        return;
                    }
                    
                    // In a real app, this would save to database
                    alert(`Motivation added successfully!\nType: ${type}\nTitle: ${title}`);
                    closeModal();
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
                        motivationCards.forEach(card => {
                            if (category === 'all' || card.getAttribute('data-category') === category) {
                                card.style.display = 'block';
                            } else {
                                card.style.display = 'none';
                            }
                        });
                    });
                });
                
                // Card click functionality
                document.querySelectorAll('.motivation-card').forEach(card => {
                    card.addEventListener('click', function(e) {
                        if (e.target.closest('.card-action-btn')) {
                            return;
                        }
                        const title = this.querySelector('.card-title').textContent;
                        const description = this.querySelector('.card-description').textContent;
                        const category = this.querySelector('.card-category').textContent;
                        
                        alert(`Motivational Content:\n\nTitle: ${title}\nCategory: ${category}\n\n${description}`);
                    });
                });
                
                // Favorite button functionality
                document.querySelectorAll('.card-action-btn.favorite').forEach(btn => {
                    btn.addEventListener('click', function(e) {
                        e.stopPropagation();
                        const icon = this.querySelector('i');
                        if (icon.className.includes('fa-star')) {
                            icon.className = 'fas fa-star';
                            this.title = 'Remove from favorites';
                        } else {
                            icon.className = 'far fa-star';
                            this.title = 'Add to favorites';
                        }
                    });
                });
                
                // Delete button functionality
                document.querySelectorAll('.card-action-btn.delete').forEach(btn => {
                    btn.addEventListener('click', function(e) {
                        e.stopPropagation();
                        const card = this.closest('.motivation-card');
                        if (confirm('Are you sure you want to delete this motivational content?')) {
                            card.style.opacity = '0';
                            card.style.transform = 'translateY(-20px)';
                            setTimeout(() => {
                                card.remove();
                            }, 300);
                        }
                    });
                });
            });
