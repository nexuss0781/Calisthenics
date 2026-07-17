// calendar.js - extracted from calander.html
        // Calendar functionality
        document.addEventListener('DOMContentLoaded', function() {
            const calendarGrid = document.getElementById('calendarGrid');
            const currentMonthElement = document.getElementById('currentMonth');
            const prevMonthBtn = document.getElementById('prevMonth');
            const nextMonthBtn = document.getElementById('nextMonth');
            
            let currentDate = new Date();
            let currentYear = currentDate.getFullYear();
            let currentMonth = currentDate.getMonth();
            
            // Days of the week
            const weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
            
            // Workout plan data (mock data)
            const workoutPlans = {
                '2025-11-08': { type: 'workout', name: 'Upper Body Blast' },
                '2025-11-09': { type: 'rest', name: 'Active Rest Day' },
                '2025-11-10': { type: 'workout', name: 'Leg Day' },
                '2025-11-12': { type: 'workout', name: 'Core & Mobility' },
                '2025-11-14': { type: 'workout', name: 'Pull-up Focus' },
                '2025-11-16': { type: 'rest', name: 'Complete Rest' },
                '2025-11-17': { type: 'workout', name: 'Full Body' },
                '2025-11-19': { type: 'workout', name: 'Push-up Progression' },
                '2025-11-21': { type: 'workout', name: 'Leg & Core' },
                '2025-11-23': { type: 'rest', name: 'Active Recovery' },
                '2025-11-24': { type: 'workout', name: 'Upper Body' },
                '2025-11-26': { type: 'workout', name: 'Skill Work' }
            };
            
            // Generate calendar
            function generateCalendar(year, month) {
                calendarGrid.innerHTML = '';
                currentMonthElement.textContent = new Date(year, month).toLocaleDateString('en-US', { month: 'long', year: 'numeric' });
                
                // Get first day of month and number of days
                const firstDay = new Date(year, month, 1).getDay();
                const daysInMonth = new Date(year, month + 1, 0).getDate();
                const daysInPrevMonth = new Date(year, month, 0).getDate();
                
                // Previous month days
                for (let i = firstDay - 1; i >= 0; i--) {
                    const day = daysInPrevMonth - i;
                    const dateStr = formatDate(new Date(year, month - 1, day));
                    const hasEvent = workoutPlans[dateStr] ? true : false;
                    const dayElement = createDayElement(day, hasEvent, 'other-month', dateStr);
                    calendarGrid.appendChild(dayElement);
                }
                
                // Current month days
                for (let day = 1; day <= daysInMonth; day++) {
                    const date = new Date(year, month, day);
                    const dateStr = formatDate(date);
                    const isToday = date.toDateString() === new Date().toDateString();
                    const hasEvent = workoutPlans[dateStr] ? true : false;
                    const dayElement = createDayElement(day, hasEvent, isToday ? 'today' : '', dateStr);
                    calendarGrid.appendChild(dayElement);
                }
                
                // Next month days to fill the grid
                const totalCells = 42; // 6 weeks * 7 days
                const remainingCells = totalCells - (firstDay + daysInMonth);
                for (let day = 1; day <= remainingCells; day++) {
                    const dateStr = formatDate(new Date(year, month + 1, day));
                    const hasEvent = workoutPlans[dateStr] ? true : false;
                    const dayElement = createDayElement(day, hasEvent, 'other-month', dateStr);
                    calendarGrid.appendChild(dayElement);
                }
            }
            
            function formatDate(date) {
                const year = date.getFullYear();
                const month = String(date.getMonth() + 1).padStart(2, '0');
                const day = String(date.getDate()).padStart(2, '0');
                return `${year}-${month}-${day}`;
            }
            
            function createDayElement(day, hasEvent, className, dateStr) {
                const dayElement = document.createElement('div');
                dayElement.className = `calendar-day ${className}`;
                dayElement.dataset.date = dateStr;
                
                dayElement.innerHTML = `
                    <div class="day-number">${day}</div>
                    ${hasEvent ? '<div class="day-events"><div class="event-indicator workout"></div></div>' : ''}
                `;
                
                // Add click event to show plan details
                dayElement.addEventListener('click', function() {
                    if (hasEvent) {
                        const plan = workoutPlans[dateStr];
                        alert(`Plan: ${plan.name}\nType: ${plan.type}\nDate: ${dateStr}`);
                    } else {
                        // Open add plan modal for this date
                        document.getElementById('addPlanModal').style.display = 'flex';
                        const dateInput = document.getElementById('planDate');
                        const selectedDate = new Date(dateStr);
                        selectedDate.setHours(19, 0, 0, 0); // Set to 7:00 PM
                        dateInput.value = selectedDate.toISOString().slice(0, 16);
                    }
                });
                
                return dayElement;
            }
            
            // Navigation
            prevMonthBtn.addEventListener('click', function() {
                currentMonth--;
                if (currentMonth < 0) {
                    currentMonth = 11;
                    currentYear--;
                }
                generateCalendar(currentYear, currentMonth);
            });
            
            nextMonthBtn.addEventListener('click', function() {
                currentMonth++;
                if (currentMonth > 11) {
                    currentMonth = 0;
                    currentYear++;
                }
                generateCalendar(currentYear, currentMonth);
            });
            
            // Initialize calendar
            generateCalendar(currentYear, currentMonth);
            
            // Add Plan Modal functionality
            const addPlanBtn = document.getElementById('addPlanBtn');
            const addPlanModal = document.getElementById('addPlanModal');
            const cancelPlanBtn = document.getElementById('cancelPlanBtn');
            const savePlanBtn = document.getElementById('savePlanBtn');
            
            addPlanBtn.addEventListener('click', function() {
                addPlanModal.style.display = 'flex';
                const now = new Date();
                now.setHours(19, 0, 0, 0); // Set to 7:00 PM
                document.getElementById('planDate').value = now.toISOString().slice(0, 16);
            });
            
            cancelPlanBtn.addEventListener('click', function() {
                addPlanModal.style.display = 'none';
            });
            
            savePlanBtn.addEventListener('click', function() {
                const planType = document.getElementById('planType').value;
                const planName = document.getElementById('planName').value.trim();
                const planDate = document.getElementById('planDate').value;
                
                if (!planName || !planDate) {
                    alert('Please fill in all fields!');
                    return;
                }
                
                // Add to workoutPlans object
                const dateKey = planDate.split('T')[0];
                workoutPlans[dateKey] = {
                    type: planType,
                    name: planName
                };
                
                // Update calendar
                generateCalendar(currentYear, currentMonth);
                
                // Close modal and reset form
                addPlanModal.style.display = 'none';
                document.getElementById('planName').value = '';
                
                alert('Plan added successfully!');
            });
            
            // Close modal when clicking outside
            addPlanModal.addEventListener('click', function(e) {
                if (e.target === addPlanModal) {
                    addPlanModal.style.display = 'none';
                }
            });
            
            // Plan action buttons
            document.querySelectorAll('.plan-action-btn.delete').forEach(btn => {
                btn.addEventListener('click', function() {
                    if (confirm('Are you sure you want to delete this plan?')) {
                        const planItem = this.closest('.plan-item');
                        planItem.style.opacity = '0';
                        planItem.style.transform = 'translateX(-20px)';
                        setTimeout(() => {
                            planItem.remove();
                        }, 300);
                    }
                });
            });
            
            document.querySelectorAll('.plan-action-btn.edit').forEach(btn => {
                btn.addEventListener('click', function() {
                    alert('Edit functionality would open a form to modify this plan.');
                });
            });
        });
