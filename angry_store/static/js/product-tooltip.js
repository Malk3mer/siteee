// تتبع الماوس وإظهار المربع
document.addEventListener('DOMContentLoaded', function() {
    const productCards = document.querySelectorAll('.product-card');
    
    productCards.forEach(card => {
        const tooltip = card.querySelector('.product-quick-desc');
        
        if (tooltip) {
            card.addEventListener('mouseenter', function() {
                tooltip.style.display = 'block';
            });
            
            card.addEventListener('mousemove', function(e) {
                const x = e.clientX + 15;
                const y = e.clientY + 15;
                
                tooltip.style.left = x + 'px';
                tooltip.style.top = y + 'px';
            });
            
            card.addEventListener('mouseleave', function() {
                tooltip.style.display = 'none';
            });
        }
    });
});
