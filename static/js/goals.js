// goals.js - extracted from Goals.html
            // Goals functionality
            document.addEventListener('DOMContentLoaded', function() {
                const addGoalBtn = document.getElementById('addGoalBtn');
                const addGoalModal = document.getElementById('addGoalModal');
                const closeModalBtn = document.getElementById('closeModal');
                const cancelGoalBtn = document.getElementById('cancelGoalBtn');
                const saveGoalBtn = document.getElementById('saveGoalBtn');
                const fileUploadArea = document.getElementById('fileUploadArea');
                const mediaFilesInput = document.getElementById('mediaFiles');
                const uploadedFilesContainer = document.getElementById('uploadedFilesContainer');
                
                // Set target date to 30 days from now
                const today = new Date();
                const targetDate = new Date(today);
                targetDate.setDate(today.getDate() + 30);
                document.getElementById('goalTargetDate').value = targetDate.toISOString().split('T')[0];
                
                // Open modal
                addGoalBtn.addEventListener('click', function() {
                    addGoalModal.style.display = 'flex';
                });
                
                // Close modal functions
                function closeModal() {
                    addGoalModal.style.display = 'none';
                    // Reset form
                    document.getElementById('goalTitle').value = '';
                    document.getElementById('goalDescription').value = '';
                    document.getElementById('goalNotes').value = '';
                    uploadedFilesContainer.innerHTML = '';
                }
                
                closeModalBtn.addEventListener('click', closeModal);
                cancelGoalBtn.addEventListener('click', closeModal);
                
                // Close modal when clicking outside
                addGoalModal.addEventListener('click', function(e) {
                    if (e.target === addGoalModal) {
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
                    const files = Array.from(this.files);
                    files.forEach(file => {
                        const fileItem = document.createElement('div');
                        fileItem.className = 'uploaded-file';
                        fileItem.innerHTML = `
                            ${file.type.startsWith('image') ? '<i class="fas fa-image"></i>' : '<i class="fas fa-video"></i>'}
                            <span>${file.name}</span>
                            <i class="fas fa-times remove-file" data-filename="${file.name}"></i>
                        `;
                        uploadedFilesContainer.appendChild(fileItem);
                    });
                    
                    // Add event listeners to remove buttons
                    document.querySelectorAll('.remove-file').forEach(btn => {
                        btn.addEventListener('click', function(e) {
                            e.stopPropagation();
                            const filename = this.getAttribute('data-filename');
                            const fileItem = this.closest('.uploaded-file');
                            fileItem.remove();
                        });
                    });
                });
                
                // Save goal
                saveGoalBtn.addEventListener('click', function() {
                    const title = document.getElementById('goalTitle').value.trim();
                    const description = document.getElementById('goalDescription').value.trim();
                    const targetDate = document.getElementById('goalTargetDate').value;
                    const notes = document.getElementById('goalNotes').value.trim();
                    
                    if (!title || !targetDate) {
                        alert('Please fill in required fields!');
                        return;
                    }
                    
                    // In a real app, this would save to database
                    const uploadedFiles = document.querySelectorAll('.uploaded-file').length;
                    alert(`Goal created successfully!\nTitle: ${title}\nTarget Date: ${targetDate}\n${uploadedFiles} files uploaded`);
                    closeModal();
                });
                
                // Goal action functionality
                document.querySelectorAll('.goal-action-btn.complete').forEach(btn => {
                    btn.addEventListener('click', function() {
                        const goalItem = this.closest('.goal-item');
                        goalItem.classList.toggle('completed');
                        const icon = this.querySelector('i');
                        const status = goalItem.querySelector('.goal-status');
                        
                        if (goalItem.classList.contains('completed')) {
                            icon.className = 'fas fa-undo';
                            status.textContent = 'Completed';
                            status.className = 'goal-status status-completed';
                        } else {
                            icon.className = 'fas fa-check';
                            status.textContent = 'In Progress';
                            status.className = 'goal-status status-in-progress';
                        }
                    });
                });
                
                document.querySelectorAll('.goal-action-btn.delete').forEach(btn => {
                    btn.addEventListener('click', function() {
                        const goalItem = this.closest('.goal-item');
                        if (confirm('Are you sure you want to delete this goal?')) {
                            goalItem.style.opacity = '0';
                            goalItem.style.transform = 'translateX(-20px)';
                            setTimeout(() => {
                                goalItem.remove();
                            }, 300);
                        }
                    });
                });
                
                // Gallery item click functionality
                document.querySelectorAll('.gallery-item').forEach(item => {
                    item.addEventListener('click', function() {
                        const title = this.querySelector('h4').textContent;
                        const description = this.querySelector('p').textContent;
                        alert(`Gallery Item:\n\n${title}\n${description}`);
                    });
                });
            });
