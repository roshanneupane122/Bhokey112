// Mobile menu toggle
  const hamburger = document.getElementById('hamburger');
  const navLinks = document.getElementById('navLinks');

  hamburger.addEventListener('click', () => {
    console.log("hello");
    navLinks.classList.toggle('active');
  });

// Image upload preview for post form
document.addEventListener('DOMContentLoaded', function() {
    const foodImagesInput = document.getElementById('food-images');
    const previewItem = document.querySelector('.preview-item.empty');

    if(foodImagesInput && previewItem) {
        foodImagesInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();

                reader.onload = function(e) {
                    previewItem.innerHTML = `<img src="${e.target.result}" alt="Food preview">`;
                    previewItem.classList.remove('empty');
                }

                reader.readAsDataURL(file);
            }
        });
    }
});


// Simple filter functionality for listings page
// document.querySelector('.btn-apply').addEventListener('click', function() {
//     const category = document.getElementById('category-filter').value;
//     const dietary = document.getElementById('dietary-filter').value;
    
   
// });

// Listing card click handler
// document.querySelectorAll('.listing-card').forEach(card => {
//     card.addEventListener('click', function(e) {
//         // Don't trigger if clicking on a button inside the card
//         if (!e.target.closest('.btn-request, .btn-outline')) {
//             // In a real app, this would navigate to the listing detail page
//             console.log('Viewing listing:', this.querySelector('h3').textContent);
//         }
//     });
// });



