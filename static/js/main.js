document.addEventListener('DOMContentLoaded', function() {
    var showCommentFormButton = document.getElementById('showCommentForm');
    var commentFormDiv = document.querySelector('.cmnt-form');
    
    showCommentFormButton.addEventListener('click', function() {
        if (commentFormDiv.style.display === 'none') {
            commentFormDiv.style.display = 'block';
        } else {
            commentFormDiv.style.display = 'none';
        }
    });
});

