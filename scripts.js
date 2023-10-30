document.addEventListener("DOMContentLoaded", function() {
    const classFilter = document.getElementById('classFilter');
    const subjectFilter = document.getElementById('subjectFilter');
    const typeFilter = document.getElementById('typeFilter');
    const materialItems = document.querySelectorAll('.material-item');

    // Функция фильтрации
    function filterMaterials() {
        const classValue = classFilter.value;
        const subjectValue = subjectFilter.value;
        const typeValue = typeFilter.value;

        materialItems.forEach(item => {
            if ((classValue === 'all' || item.getAttribute('data-class') === classValue) && 
                (subjectValue === 'all' || item.getAttribute('data-subject') === subjectValue) && 
                (typeValue === 'all' || item.getAttribute('data-type') === typeValue)) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    }

    // Слушатели событий для выпадающих списков
    classFilter.addEventListener('change', filterMaterials);
    subjectFilter.addEventListener('change', filterMaterials);
    typeFilter.addEventListener('change', filterMaterials);
});
