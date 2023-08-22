$(document).ready(function () {
  $(".customer-logos").slick({
    slidesToShow: 6,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 1500,
    arrows: false,
    dots: false,
    pauseOnHover: false,
    responsive: [
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 4,
        },
      },
      {
        breakpoint: 520,
        settings: {
          slidesToShow: 3,
        },
      },
    ],
  });
});

// document.addEventListener("DOMContentLoaded", function () {
//   const filterDropdown = document.getElementById("filterDropdown");
//   const filterItems = document.querySelectorAll(".filter-item");

//   filterDropdown.addEventListener("change", function () {
//     const selectedValue = filterDropdown.value;

//     filterItems.forEach(function (item) {
//       if (selectedValue === "all") {
//         item.style.display = "block";
//       } else if (item.classList.contains(selectedValue)) {
//         item.style.display = "block";
//       } else {
//         item.style.display = "none";
//       }
//     });
//   });
// });
