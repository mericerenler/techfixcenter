/* 
   Minimal JavaScript
   Currently empty to ensure maximum speed and "clean" feel.
   Add interactivity here only if absolutely necessary (e.g. mobile menu toggle).
*/

console.log('Site loaded securely.');

// Client-Side Search for Device Problems Page
document.addEventListener('DOMContentLoaded', function () {
   const searchInput = document.getElementById('deviceSearch');

   if (searchInput) {
      searchInput.addEventListener('keyup', function (e) {
         const term = e.target.value.toLowerCase();

         // Target both lists (iPhone and General)
         const listItems = document.querySelectorAll('.category-articles li');

         listItems.forEach(function (item) {
            const text = item.textContent.toLowerCase();
            if (text.includes(term)) {
               item.style.display = '';
            } else {
               item.style.display = 'none';
            }
         });
      });
   }
});
