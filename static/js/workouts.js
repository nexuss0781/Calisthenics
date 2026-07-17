// workouts.js - extracted from Workouts.html
        // Card expansion functionality
        document.querySelectorAll('.exercise-card').forEach(card => {
            card.addEventListener('click', function(e) {
                // Check if clicked on action buttons
                if (e.target.closest('.action-btn')) {
                    return;
                }
                
                // Toggle expanded state
                const isExpanded = this.classList.contains('expanded');
                
                // Collapse all other cards
                document.querySelectorAll('.exercise-card').forEach(otherCard => {
                    otherCard.classList.remove('expanded');
                });
                
                // Expand current card if not already expanded
                if (!isExpanded) {
                    this.classList.add('expanded');
                }
            });
        });

        // Action button functionality
        document.querySelectorAll('.action-btn.delete').forEach(btn => {
            btn.addEventListener('click', function(e) {
                e.stopPropagation();
                const card = this.closest('.exercise-card');
                if (confirm('Are you sure you want to delete this exercise?')) {
                    card.style.opacity = '0';
                    card.style.transform = 'translateX(-20px)';
                    setTimeout(() => {
                        card.remove();
                    }, 300);
                }
            });
        });

        document.querySelectorAll('.action-btn.edit').forEach(btn => {
            btn.addEventListener('click', function(e) {
                e.stopPropagation();
                const card = this.closest('.exercise-card');
                alert('Edit functionality would open a form to modify this exercise.');
                // In a real app, this would open an edit form
            });
        });

        // Add Exercise Form Toggle
        document.getElementById('addExerciseBtn').addEventListener('click', function() {
            const form = document.getElementById('addExerciseForm');
            if (form.style.display === 'none' || form.style.display === '') {
                form.style.display = 'block';
                this.innerHTML = '<i class="fas fa-times"></i> Cancel';
                this.style.backgroundColor = '#d63031';
                this.style.borderColor = '#d63031';
            } else {
                form.style.display = 'none';
                this.innerHTML = '<i class="fas fa-plus"></i> Add Exercise';
                this.style.backgroundColor = '#ff6b35';
                this.style.borderColor = '#ff6b35';
            }
        });

        // Cancel Exercise Form
        document.getElementById('cancelExerciseBtn').addEventListener('click', function() {
            document.getElementById('addExerciseForm').style.display = 'none';
            document.getElementById('addExerciseBtn').innerHTML = '<i class="fas fa-plus"></i> Add Exercise';
            document.getElementById('addExerciseBtn').style.backgroundColor = '#ff6b35';
            document.getElementById('addExerciseBtn').style.borderColor = '#ff6b35';
        });

        // Save Exercise
        document.getElementById('saveExerciseBtn').addEventListener('click', function() {
            const name = document.getElementById('exerciseName').value.trim();
            const sets = document.getElementById('sets').value;
            const reps = document.getElementById('reps').value;
            const difficulty = document.getElementById('difficulty').value;
            
            if (!name || !sets || !reps || !difficulty) {
                alert('Please fill in all fields!');
                return;
            }
            
            // Create new exercise card
            const workoutsGrid = document.querySelector('.workouts-grid');
            const difficultyClass = `difficulty-${difficulty.toLowerCase()}`;
            
            const newCard = document.createElement('div');
            newCard.className = 'exercise-card';
            newCard.innerHTML = `
                <div class="card-header">
                    <div class="exercise-name">${name}</div>
                    <div class="exercise-difficulty ${difficultyClass}">${difficulty}</div>
                </div>
                <div class="exercise-stats">
                    <div class="stat-item">
                        <div class="stat-value">${sets}</div>
                        <div class="stat-label">Sets</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">${reps}</div>
                        <div class="stat-label">${reps > 1 ? 'Reps' : 'Rep'}</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">2m</div>
                        <div class="stat-label">Rest</div>
                    </div>
                </div>
                
                <div class="expanded-content">
                    <div class="workout-plan">
                        <h4>Weekly Workout Plan</h4>
                        <div class="workout-days">
                            <div class="day-card">
                                <div class="day-name">Mon</div>
                                <div class="day-status">Scheduled</div>
                            </div>
                            <div class="day-card">
                                <div class="day-name">Wed</div>
                                <div class="day-status">Scheduled</div>
                            </div>
                            <div class="day-card">
                                <div class="day-name">Fri</div>
                                <div class="day-status">Scheduled</div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="exercise-details">
                        <h4>Exercise Details</h4>
                        <ul class="exercise-steps">
                            <li>Exercise details will be added here</li>
                            <li>Proper form instructions</li>
                        </ul>
                    </div>
                    
                    <div class="card-actions">
                        <button class="action-btn edit"><i class="fas fa-edit"></i> Edit</button>
                        <button class="action-btn delete"><i class="fas fa-trash"></i> Delete</button>
                    </div>
                </div>
            `;
            
            workoutsGrid.appendChild(newCard);
            
            // Reset and hide form
            document.getElementById('addExerciseForm').style.display = 'none';
            document.getElementById('addExerciseBtn').innerHTML = '<i class="fas fa-plus"></i> Add Exercise';
            document.getElementById('addExerciseBtn').style.backgroundColor = '#ff6b35';
            document.getElementById('addExerciseBtn').style.borderColor = '#ff6b35';
            
            // Reset form
            document.getElementById('exerciseName').value = '';
            document.getElementById('sets').value = '3';
            document.getElementById('reps').value = '15';
            document.getElementById('difficulty').value = '';
            
            // Add event listeners to new card
            newCard.addEventListener('click', function(e) {
                if (e.target.closest('.action-btn')) {
                    return;
                }
                document.querySelectorAll('.exercise-card').forEach(otherCard => {
                    otherCard.classList.remove('expanded');
                });
                this.classList.add('expanded');
            });
            
            // Add event listeners to action buttons
            newCard.querySelector('.action-btn.delete').addEventListener('click', function(e) {
                e.stopPropagation();
                const card = this.closest('.exercise-card');
                if (confirm('Are you sure you want to delete this exercise?')) {
                    card.style.opacity = '0';
                    card.style.transform = 'translateX(-20px)';
                    setTimeout(() => {
                        card.remove();
                    }, 300);
                }
            });
            
            newCard.querySelector('.action-btn.edit').addEventListener('click', function(e) {
                e.stopPropagation();
                alert('Edit functionality would open a form to modify this exercise.');
            });
            
            alert('Exercise added successfully!');
        });

        // Close expanded card when clicking outside
        document.addEventListener('click', function(e) {
            if (!e.target.closest('.exercise-card')) {
                document.querySelectorAll('.exercise-card').forEach(card => {
                    card.classList.remove('expanded');
                });
            }
        });
