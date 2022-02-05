const createDav = () => {
    let nav = document.querySelector('.navbar');
    nav.innerHTML = `
    <div class="nav">
   <img src="{% static '../images/dark-logo.png' %}" class="brand-logo" alt="love">
<div class="nav-items">
   <div class="search">
   <input type="text" class="search-box" placeholder="search 1place">
   <button class="search-btn">search</button>
   <a href="#"><img src="{% static '../images/cart.png' %}" alt="add"></a>
   </div>
</div>
</div>

<ul class="links-containers">
<li class="link-item"><a href="" class="link">home</a></li>
<li class="link-item"><a href="" class="link">home</a></li>
<li class="link-item"><a href="" class="link">home</a></li>
<li class="link-item"><a href="" class="link">home</a></li>
</ul>
`;
}
createDav();
