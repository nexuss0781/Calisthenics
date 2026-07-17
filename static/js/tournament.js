// tournament.js - extracted from Tournament.html
            // Tournament functionality
            document.addEventListener('DOMContentLoaded', function() {
                const joinTournamentBtn = document.getElementById('joinTournamentBtn');
                const joinTournamentModal = document.getElementById('joinTournamentModal');
                const cancelJoinBtn = document.getElementById('cancelJoinBtn');
                const confirmJoinBtn = document.getElementById('confirmJoinBtn');
                
                // Open join tournament modal
                joinTournamentBtn.addEventListener('click', function() {
                    joinTournamentModal.style.display = 'flex';
                });
                
                // Close modal functions
                function closeJoinModal() {
                    joinTournamentModal.style.display = 'none';
                }
                
                cancelJoinBtn.addEventListener('click', closeJoinModal);
                confirmJoinBtn.addEventListener('click', function() {
                    alert('You have successfully joined the tournament! Check your email for details.');
                    closeJoinModal();
                });
                
                // Close modal when clicking outside
                joinTournamentModal.addEventListener('click', function(e) {
                    if (e.target === joinTournamentModal) {
                        closeJoinModal();
                    }
                });
                
                // Challenge button functionality
                document.querySelectorAll('.challenge-btn.start').forEach(btn => {
                    btn.addEventListener('click', function() {
                        const challengeTitle = this.closest('.challenge-item').querySelector('.challenge-title').textContent;
                        if (this.textContent === 'Start Challenge') {
                            alert(`Starting challenge: ${challengeTitle}\n\nGet ready to push your limits!`);
                        } else if (this.textContent === 'Unlock') {
                            alert(`Challenge unlocked: ${challengeTitle}\n\nYou can now attempt this challenge!`);
                        }
                    });
                });
                
                // Calendar day click functionality
                document.querySelectorAll('.calendar-day').forEach(day => {
                    day.addEventListener('click', function() {
                        if (this.classList.contains('tournament') || this.classList.contains('completed') || this.classList.contains('today')) {
                            const dayNumber = this.textContent.trim();
                            if (this.classList.contains('completed')) {
                                alert(`Tournament completed on November ${dayNumber}, 2025\nResult: Victory! 🏆`);
                            } else if (this.classList.contains('tournament')) {
                                alert(`Tournament scheduled for November ${dayNumber}, 2025\nGet ready to compete!`);
                            } else if (this.classList.contains('today')) {
                                alert(`Today is November ${dayNumber}, 2025\nNo tournament scheduled today.`);
                            }
                        }
                    });
                });
                
                // Challenge item click functionality
                document.querySelectorAll('.challenge-item').forEach(item => {
                    item.addEventListener('click', function(e) {
                        if (e.target.closest('.challenge-btn')) {
                            return;
                        }
                        const title = this.querySelector('.challenge-title').textContent;
                        const level = this.querySelector('.challenge-level').textContent;
                        const details = this.querySelector('.challenge-details').textContent;
                        
                        alert(`Challenge Details:\n\n${title}\n${level}\n\nClick the action button to participate!`);
                    });
                });
            });
