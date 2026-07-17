// plan.js - extracted from Plan.html
            // Plan functionality
            document.addEventListener('DOMContentLoaded', function() {
                const addPlanBtn = document.getElementById('addPlanBtn');
                const addPlanModal = document.getElementById('addPlanModal');
                const closeModalBtn = document.getElementById('closeModal');
                const cancelPlanBtn = document.getElementById('cancelPlanBtn');
                const savePlanBtn = document.getElementById('savePlanBtn');
                
                // Set date inputs to current month
                const today = new Date();
                const startDate = new Date(today.getFullYear(), today.getMonth(), 1);
                const endDate = new Date(today.getFullYear(), today.getMonth() + 1, 0);
                
                document.getElementById('planStartDate').value = startDate.toISOString().split('T')[0];
                document.getElementById('planEndDate').value = endDate.toISOString().split('T')[0];
                
                // Open modal
                addPlanBtn.addEventListener('click', function() {
                    addPlanModal.style.display = 'flex';
                });
                
                // Close modal functions
                function closeModal() {
                    addPlanModal.style.display = 'none';
                    // Reset form
                    document.getElementById('planTitle').value = '';
                    document.getElementById('planType').value = '';
                    document.getElementById('planDescription').value = '';
                }
                
                closeModalBtn.addEventListener('click', closeModal);
                cancelPlanBtn.addEventListener('click', closeModal);
                
                // Close modal when clicking outside
                addPlanModal.addEventListener('click', function(e) {
                    if (e.target === addPlanModal) {
                        closeModal();
                    }
                });
                
                // Save plan
                savePlanBtn.addEventListener('click', function() {
                    const title = document.getElementById('planTitle').value.trim();
                    const type = document.getElementById('planType').value;
                    const startDate = document.getElementById('planStartDate').value;
                    const endDate = document.getElementById('planEndDate').value;
                    const description = document.getElementById('planDescription').value.trim();
                    
                    if (!title || !type || !startDate || !endDate || !description) {
                        alert('Please fill in all required fields!');
                        return;
                    }
                    
                    // In a real app, this would save to database
                    alert(`Plan created successfully!\nTitle: ${title}\nType: ${type}\nDuration: ${startDate} to ${endDate}`);
                    closeModal();
                    
                    // In a real implementation, you would add the new plan to the UI
                });
                
                // Plan card click functionality
                document.querySelectorAll('.plan-item-card').forEach(card => {
                    card.addEventListener('click', function(e) {
                        if (e.target.closest('.plan-action-btn')) {
                            return;
                        }
                        const title = this.querySelector('.plan-item-title').textContent;
                        const description = this.querySelector('.plan-item-details p').textContent;
                        const date = this.querySelector('.plan-item-date').textContent;
                        const status = this.querySelector('.plan-item-status').textContent;
                        
                        alert(`Plan Details:\n\nTitle: ${title}\nStatus: ${status}\n${date}\n\nDescription: ${description}`);
                    });
                });
                
                // Edit button functionality
                document.querySelectorAll('.plan-action-btn.edit').forEach(btn => {
                    btn.addEventListener('click', function(e) {
                        e.stopPropagation();
                        alert('Edit functionality would open a form to modify this plan.');
                    });
                });
                
                // Delete button functionality
                document.querySelectorAll('.plan-action-btn.delete').forEach(btn => {
                    btn.addEventListener('click', function(e) {
                        e.stopPropagation();
                        const card = this.closest('.plan-item-card');
                        if (confirm('Are you sure you want to delete this plan?')) {
                            card.style.opacity = '0';
                            card.style.transform = 'translateX(-20px)';
                            setTimeout(() => {
                                card.remove();
                            }, 300);
                        }
                    });
                });
                
                // Calendar day click functionality
                document.querySelectorAll('.calendar-day').forEach(day => {
                    day.addEventListener('click', function() {
                        if (this.classList.contains('planned') || this.classList.contains('completed') || this.classList.contains('today')) {
                            const dayNumber = this.textContent;
                            const status = this.classList.contains('completed') ? 'completed' : 
                                         this.classList.contains('planned') ? 'planned' : 'today';
                            alert(`Plan activities for November ${dayNumber}, 2025\nStatus: ${status}`);
                        } else {
                            alert(`No plans scheduled for November ${this.textContent}, 2025`);
                        }
                    });
                });
            });
