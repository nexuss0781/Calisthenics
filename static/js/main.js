document.addEventListener('DOMContentLoaded', function() {
    // Modal utility functions
    window.openModal = function(id) {
        var modal = document.getElementById(id);
        if (modal) modal.style.display = 'flex';
    };

    window.closeModal = function(id) {
        var modal = document.getElementById(id);
        if (modal) modal.style.display = 'none';
    };

    // Close modal on outside click
    document.querySelectorAll('.add-goal-modal, .add-schedule-modal, .add-exercise-form, .add-plan-modal, .add-motivation-modal, .video-player-modal, .upload-modal').forEach(function(modal) {
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                modal.style.display = 'none';
            }
        });
    });

    // Close modal buttons
    document.querySelectorAll('.close-modal, .cancel-btn').forEach(function(btn) {
        btn.addEventListener('click', function() {
            var modal = this.closest('.add-goal-modal, .add-schedule-modal, .add-exercise-form, .add-plan-modal, .add-motivation-modal, .video-player-modal, .upload-modal');
            if (modal) modal.style.display = 'none';
        });
    });
});
