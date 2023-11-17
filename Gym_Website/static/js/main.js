$(document).ready(function () {

  $(".banner-carousel").owlCarousel({
    animateOut: "fadeOut",
    animateIn: "flipInX",
    items: 1,
    smartSpeed: 450,
    nav: true,
    loop: true,
    dots: false,
    mouseDrag: false,
    touchDrag: false,
  });


  $(".team-carousel").owlCarousel({
    loop: true,
    margin: 30,
    responsive: {
      0: {
        items: 1,
      },
      600: {
        items: 2,
      },
      1000: {
        items: 3,
      },
    },
  });

  $(".honor-carousel").owlCarousel({

    loop: true,
    autoplay: true,
    items: 1,
    nav: true,
  });



  $(".overlay-gallery").magnificPopup({
    delegate: "a",
    type: "image",
    closeMarkup: '<button  class="mfp-close" style=" right: 8px"><img src="static/images/close.png" class="mfp-close" style="width:50px;height:50px"/></button>',
    gallery: {
      enabled: true,
      arrowMarkup: '<img class="mfp-arrow custom-mfp-arrow-%dir%" src="static/images/arrow.png" style="margin:0"/>',
      tPrev: "Previous",
      tNext: "Next",
      tCounter: '<span  style="color:red; font-size:17px" class="mfp-counter">%curr% of %total%</span>',
    },
    zoom: {
      enabled: true,
      duration: 300,
      easing: "ease-in-out",
      opener: function (openerElement) {
        return openerElement.is("img") ?
          openerElement :
          openerElement.find("img");
      },
    },
  });

  $(".pics").magnificPopup({
    delegate: "a",
    type: "image",
    closeMarkup: '<button  class="mfp-close" style=" right: 8px"><img src="../static/images/close.png" class="mfp-close" style="width:50px;height:50px"/></button>',
    gallery: {
      enabled: true,
      arrowMarkup: '<img class="mfp-arrow custom-mfp-arrow-%dir%" src="../static/images/arrow.png" style="margin:0"/>',
      tPrev: "Previous",
      tNext: "Next",
      tCounter: '<span  style="color:red; font-size:17px" class="mfp-counter">%curr% of %total%</span>',
    },
    zoom: {
      enabled: true,
      duration: 300,
      easing: "ease-in-out",
      opener: function (openerElement) {
        return openerElement.is("img") ?
          openerElement :
          openerElement.find("img");
      },
    },
  });


  setTimeout(function () {
    $('#message').fadeOut('slow');
  }, 3000);


  $(".menu").click(function () {
    $(".pages").toggleClass("active");
  });

  $("#close").on("click", function () {
    $.magnificPopup.close();
  });


  $(function () {
    var selectedClass = "";
    $(".filter").click(function () {
      selectedClass = $(this).attr("data-rel");
      if (selectedClass == "all") {
        $(".gallery-item").addClass("pics").removeClass("filter-gallery");
      } else {
        $(".gallery-item").addClass("filter-gallery").removeClass("pics");
      }
      $("#gallery").fadeTo(100, 0.1);
      $("#gallery div")
        .not("." + selectedClass)
        .fadeOut()
        .removeClass("animation");
      setTimeout(function () {
        $("." + selectedClass)
          .fadeIn()
          .addClass("animation");
        $("#gallery").fadeTo(300, 1);
      }, 300);
    });
  });

  $('.textarea').on('input', function () {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';
  });

  const toUp = document.querySelector('.scrollup');
  window.addEventListener('scroll', () => {
    if (window.pageYOffset > 1000) {
      toUp.classList.add("active");
    } else {
      toUp.classList.remove("active");
    }
  });
});

function schedule(evt, button) {
  var i, tabcontent, tablinks;

  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  document.getElementById(button).style.display = "block";
  evt.currentTarget.className += " active";
}

function filterActive(evt) {
  var i, filters;

  filters = document.getElementsByClassName("filter-check");
  for (i = 0; i < filters.length; i++) {
    filters[i].className = filters[i].className.replace("active-filter filter-check", "filter filter-check");
  }
  evt.currentTarget.className = ("filter filter-check", "active-filter filter-check");

}