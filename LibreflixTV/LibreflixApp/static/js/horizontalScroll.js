
const scrollContainers = document.querySelectorAll('.scroll-container');

scrollContainers.forEach(function(scrollContainer) {
scrollContainer.addEventListener('wheel', function(e) {
    if (e.deltaY !== 0) {
    scrollContainer.scrollLeft += e.deltaY;  // Rolagem horizontal
    e.preventDefault(); // Previne a rolagem vertical padrão
    }
});
});