function popup(id) {
    const popup = document.getElementById(id);
    const backdrop = document.querySelector('.backdrop');
    
    if(popup.style.display === 'block') {
        closePopup();
    } else {
        openPopup();
    }

    function openPopup() {
        popup.style.display = 'block';
        backdrop.style.display = 'block';
        
        popup.style.animation = "fadeIn 0.5s forwards";
        backdrop.style.animation = "fadeIn 0.5s forwards";
    }

    function closePopup() {
        popup.style.animation = "fadeOut 0.5s forwards";
        backdrop.style.animation = "fadeOut 0.5s forwards";

        setTimeout(function() {
            popup.style.display = 'none';
            backdrop.style.display = 'none';
        }, 500);
    }
}