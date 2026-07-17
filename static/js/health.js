// health.js - extracted from Health.html
            // Health data storage (in memory - persists during session)
            let healthRecords = [
                { date: '2025-11-01', weight: 75.2, bodyFat: 14.2, performance: 'Good energy, completed full workout' },
                { date: '2025-10-15', weight: 75.8, bodyFat: 14.5, performance: 'Slightly tired, reduced intensity' },
                { date: '2025-10-01', weight: 76.1, bodyFat: 14.8, performance: 'Excellent performance, PR on pull-ups' },
                { date: '2025-09-15', weight: 76.5, bodyFat: 15.1, performance: 'Recovery day, light mobility work' },
                { date: '2025-09-01', weight: 77.0, bodyFat: 15.5, performance: 'Started new program, feeling good' }
            ];

            // Health functionality
            document.addEventListener('DOMContentLoaded', function() {
                const addHealthRecordBtn = document.getElementById('addHealthRecordBtn');
                const addRecordModal = document.getElementById('addRecordModal');
                const closeRecordModal = document.getElementById('closeRecordModal');
                const cancelRecordBtn = document.getElementById('cancelRecordBtn');
                const saveRecordBtn = document.getElementById('saveRecordBtn');
                const exportDataBtn = document.getElementById('exportDataBtn');
                
                // Set current date in record form
                const today = new Date().toISOString().split('T')[0];
                document.getElementById('recordDate').value = today;
                
                // Open modal
                addHealthRecordBtn.addEventListener('click', function() {
                    addRecordModal.style.display = 'flex';
                });
                
                // Close modal functions
                function closeRecordModalFunc() {
                    addRecordModal.style.display = 'none';
                    // Reset form
                    document.getElementById('recordWeight').value = '';
                    document.getElementById('recordBodyFat').value = '';
                    document.getElementById('recordPerformance').value = '';
                }
                
                closeRecordModal.addEventListener('click', closeRecordModalFunc);
                cancelRecordBtn.addEventListener('click', closeRecordModalFunc);
                
                // Close modal when clicking outside
                addRecordModal.addEventListener('click', function(e) {
                    if (e.target === addRecordModal) {
                        closeRecordModalFunc();
                    }
                });
                
                // Save health record
                saveRecordBtn.addEventListener('click', function() {
                    const weight = document.getElementById('recordWeight').value;
                    const bodyFat = document.getElementById('recordBodyFat').value;
                    const performance = document.getElementById('recordPerformance').value;
                    const date = document.getElementById('recordDate').value;
                    
                    if (!weight || !date) {
                        alert('Please fill in required fields!');
                        return;
                    }
                    
                    // Add to health records array
                    healthRecords.push({
                        date: date,
                        weight: parseFloat(weight),
                        bodyFat: bodyFat ? parseFloat(bodyFat) : null,
                        performance: performance || 'No notes'
                    });
                    
                    alert(`Health record saved!\nWeight: ${weight}kg\nBody Fat: ${bodyFat || 'N/A'}%\nDate: ${date}`);
                    closeRecordModalFunc();
                    
                    // Update calendar to show measured days
                    updateCalendarMeasuredDays();
                });
                
                // Export data to text file
                exportDataBtn.addEventListener('click', function() {
                    if (healthRecords.length === 0) {
                        alert('No health records to export!');
                        return;
                    }
                    
                    // Create text content
                    let textContent = 'CALISTHENICS HEALTH DATA\n';
                    textContent += '========================\n\n';
                    
                    // Add basic info
                    const weight = document.getElementById('weight').value;
                    const height = document.getElementById('height').value;
                    const age = document.getElementById('age').value;
                    const gender = document.getElementById('gender').value;
                    
                    textContent += 'BASIC INFORMATION:\n';
                    textContent += `Weight: ${weight} kg\n`;
                    textContent += `Height: ${height} cm\n`;
                    textContent += `Age: ${age} years\n`;
                    textContent += `Gender: ${gender}\n`;
                    textContent += `BMI: ${calculateBMI(weight, height)}\n\n`;
                    
                    // Add health records
                    textContent += 'HEALTH RECORDS:\n';
                    textContent += 'Date,Weight(kg),BodyFat(%),Performance\n';
                    
                    // Sort records by date (newest first)
                    const sortedRecords = [...healthRecords].sort((a, b) => new Date(b.date) - new Date(a.date));
                    
                    sortedRecords.forEach(record => {
                        textContent += `${record.date},${record.weight},${record.bodyFat || 'N/A'},"${record.performance}"\n`;
                    });
                    
                    // Create and download file
                    const blob = new Blob([textContent], { type: 'text/plain' });
                    const url = URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = `calisthenics_health_data_${new Date().toISOString().split('T')[0]}.txt`;
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                    URL.revokeObjectURL(url);
                    
                    alert('Health data exported successfully! Check your downloads folder.');
                });
                
                // Plan item functionality
                document.querySelectorAll('.plan-action-btn.complete').forEach(btn => {
                    btn.addEventListener('click', function() {
                        const planItem = this.closest('.plan-item');
                        planItem.classList.toggle('completed');
                        const icon = this.querySelector('i');
                        if (planItem.classList.contains('completed')) {
                            icon.className = 'fas fa-undo';
                            this.title = 'Mark as incomplete';
                        } else {
                            icon.className = 'fas fa-check';
                            this.title = 'Mark as complete';
                        }
                    });
                });
                
                document.querySelectorAll('.plan-action-btn.delete').forEach(btn => {
                    btn.addEventListener('click', function() {
                        const planItem = this.closest('.plan-item');
                        if (confirm('Are you sure you want to delete this health plan item?')) {
                            planItem.style.opacity = '0';
                            planItem.style.transform = 'translateX(-20px)';
                            setTimeout(() => {
                                planItem.remove();
                            }, 300);
                        }
                    });
                });
                
                // Calendar day click functionality
                document.querySelectorAll('.calendar-day').forEach(day => {
                    day.addEventListener('click', function() {
                        if (this.classList.contains('measured') || this.classList.contains('today')) {
                            const dayNumber = this.textContent;
                            alert(`Health measurements recorded for November ${dayNumber}, 2025`);
                        } else {
                            alert(`No health measurements recorded for November ${this.textContent}, 2025`);
                        }
                    });
                });
                
                // Initialize calendar
                updateCalendarMeasuredDays();
            });
            
            function calculateBMI(weight, height) {
                // weight in kg, height in cm
                const heightM = parseFloat(height) / 100;
                const bmi = parseFloat(weight) / (heightM * heightM);
                return bmi.toFixed(1);
            }
            
            function updateCalendarMeasuredDays() {
                // Get all dates from health records
                const recordedDates = healthRecords.map(record => {
                    const date = new Date(record.date);
                    return date.getDate().toString();
                });
                
                // Add 'measured' class to calendar days that have records
                document.querySelectorAll('.calendar-day').forEach(day => {
                    const dayNumber = day.textContent;
                    if (recordedDates.includes(dayNumber)) {
                        day.classList.add('measured');
                    }
                });
            }
