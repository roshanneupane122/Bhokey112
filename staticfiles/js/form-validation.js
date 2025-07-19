// Form validation for post food form
document.getElementById('food-post-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Basic validation
    const foodName = document.getElementById('food-name').value;
    const foodCategory = document.getElementById('food-category').value;
    const quantity = document.getElementById('food-quantity').value;
    const prepDate = document.getElementById('prep-date').value;
    const expiryDate = document.getElementById('expiry-date').value;
    const pickupLocation = document.getElementById('pickup-location').value;
    const pickupDate = document.getElementById('pickup-date').value;
    const pickupTime = document.getElementById('pickup-time').value;
    const contactMethod = document.getElementById('contact-method').value;
    
    if (!foodName || !foodCategory || !quantity || !prepDate || !expiryDate || 
        !pickupLocation || !pickupDate || !pickupTime || !contactMethod) {
        alert('Please fill in all required fields');
        return;
    }
    
    // Date validation
    const today = new Date().toISOString().split('T')[0];
    if (prepDate > today) {
        alert('Preparation date cannot be in the future');
        return;
    }
    
    if (expiryDate < today) {
        alert('This food has already expired. Please dispose of it properly.');
        return;
    }
    
    if (pickupDate < today) {
        alert('Pickup date cannot be in the past');
        return;
    }
    
    // In a real app, this would submit to the server
    alert('Food listing submitted successfully!');
    this.reset();
    
    // Clear image previews
    document.querySelectorAll('.preview-item').forEach(item => {
        if (!item.classList.contains('empty')) {
            item.innerHTML = '<i class="fas fa-camera"></i><p>Add photo</p>';
            item.classList.add('empty');
        }
    });
});
