// schedule.js - extracted from Schedule.html
            // Schedule functionality
            document.addEventListener('DOMContentLoaded', function() {
                const addScheduleBtn = document.getElementById('addScheduleBtn');
                const addScheduleModal = document.getElementById('addScheduleModal');
                const closeModalBtn = document.getElementById('closeModal');
                const cancelScheduleBtn = document.getElementById('cancelScheduleBtn');
                const saveScheduleBtn = document.getElementById('saveScheduleBtn');
                
                // Open modal
                addScheduleBtn.addEventListener('click', function() {
                    addScheduleModal.style.display = 'flex';
                });
                
                // Close modal functions
                function closeModal() {
                    addScheduleModal.style.display = 'none';
                    // Reset form
                    document.getElementById('scheduleName').value = '';
                    document.getElementById('scheduleDetails').value = '';
                    document.getElementById('scheduleType').value = 'workout';
                }
                
                closeModalBtn.addEventListener('click', closeModal);
                cancelScheduleBtn.addEventListener('click', closeModal);
                
                // Close modal when clicking outside
                addScheduleModal.addEventListener('click', function(e) {
                    if (e.target === addScheduleModal) {
                        closeModal();
                    }
                });
                
                // Save schedule
                saveScheduleBtn.addEventListener('click', function() {
                    const scheduleType = document.getElementById('scheduleType').value;
                    const scheduleName = document.getElementById('scheduleName').value.trim();
                    const scheduleDay = document.getElementById('scheduleDay').value;
                    const scheduleTime = document.getElementById('scheduleTime').value;
                    const scheduleDetails = document.getElementById('scheduleDetails').value.trim();
                    
                    if (!scheduleName) {
                        alert('Please enter a schedule name!');
                        return;
                    }
                    
                    // In a real app, this would add to the schedule data
                    // For demo, just show success message
                    alert(`Schedule "${scheduleName}" added successfully for ${scheduleDay} at ${scheduleTime}!`);
                    closeModal();
                });
                
                // Schedule item click functionality
                document.querySelectorAll('.schedule-item').forEach(item => {
                    item.addEventListener('click', function() {
                        const name = this.querySelector('.item-name').textContent;
                        const time = this.querySelector('.item-time').textContent;
                        const details = this.querySelector('.item-type').textContent;
                        alert(`Schedule Details:\n\nName: ${name}\nTime: ${time}\nDetails: ${details}`);
                    });
                });
                
                // Sticky note functionality
                document.querySelectorAll('.sticky-note').forEach(note => {
                    note.addEventListener('click', function(e) {
                        if (e.target.closest('.sticky-action')) {
                            return;
                        }
                        const title = this.querySelector('h4').textContent;
                        const content = this.querySelector('p').textContent;
                        alert(`Sticky Note:\n\n${title}\n\n${content}`);
                    });
                });
                
                // Sticky note delete functionality
                document.querySelectorAll('.sticky-action').forEach(action => {
                    if (action.innerHTML.includes('fa-trash')) {
                        action.addEventListener('click', function(e) {
                            e.stopPropagation();
                            const note = this.closest('.sticky-note');
                            if (confirm('Are you sure you want to delete this sticky note?')) {
                                note.style.opacity = '0';
                                note.style.transform = 'translateY(-20px)';
                                setTimeout(() => {
                                    note.remove();
                                }, 300);
                            }
                        });
                    }
                });
                
                // Sticky note edit functionality
                document.querySelectorAll('.sticky-action').forEach(action => {
                    if (action.innerHTML.includes('fa-edit')) {
                        action.addEventListener('click', function(e) {
                            e.stopPropagation();
                            alert('Edit functionality would open a form to modify this sticky note.');
                        });
                    }
                });
            });
