//javascript code for search bar
let searchForm = document.querySelector(".search-form");
document.querySelector("#search-btn").onclick = () => {
  searchForm.classList.toggle("active");
  //logonForm.classList.remove("active");
  menulist.classList.remove("active");
};
/*
 //javascript code for login form
let logonForm =document.querySelector(".login-form");
document.querySelector('#login-btn').onclick = () =>
{ 
    searchForm.classList.remove('active');
    logonForm.classList.toggle('active');
    menulist.classList.remove('active');
}
*/
// javascript code for menu list
let menulist = document.querySelector(".navbar");
document.querySelector("#menu-btn").onclick = () => {
  menulist.classList.toggle("active");
  searchForm.classList.remove("active");
  //logonForm.classList.remove("active");
};

window.onscroll = () => {
  searchForm.classList.remove("active");
  //logonForm.classList.remove("active");
  menulist.classList.remove("active");
};
/*
// javascript code for product detail
 // Add your JavaScript code here
 window.addEventListener('DOMContentLoaded', () => {
    const products = document.querySelectorAll('.product');

    products.forEach((product) => {
      const viewDetailsLink = product.querySelector('a');
      const detailsContainer = product.querySelector('.details');

      viewDetailsLink.addEventListener('click', (event) => {
        event.preventDefault();
        detailsContainer.classList.toggle('active');
      });
    });
  });
  */
