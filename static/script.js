const btnMenu = document.querySelector('.btn_menu')
const btnBar = document.querySelector('.btn_bar')
const header = document.querySelector('.header')
const menuCategories = document.querySelector('.menu-categories')
const barCategories = document.querySelector('.bar-categories')
let mybutton = document.getElementById("myBtn");
const barMenu = document.querySelector('.bar-menu')
const foodMenu = document.querySelector('.food-menu')

btnMenu.addEventListener('click', () => {
    header.classList.remove('header-bar_menu')
    header.classList.add('meal-menu')
    menuCategories.style.display = 'flex'
    barCategories.style.display = 'none'
    foodMenu.style.display = 'flex'
    barMenu.style.display = 'none'
    mybutton.style.backgroundColor = 'rgba(214, 94, 27, 0.50)'
})

btnBar.addEventListener('click', () => {
    header.classList.remove('meal-menu')
    header.classList.add('header-bar_menu')
    menuCategories.style.display = 'none'
    barCategories.style.display = 'flex'
    foodMenu.style.display = 'none'
    barMenu.style.display = 'flex'
    mybutton.style.backgroundColor = '#545BFF'
})

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 1500 || document.documentElement.scrollTop > 1500) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}