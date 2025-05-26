visibleMenu = document.querySelectorAll(".visible");
hiddenMenu = document.querySelectorAll(".hidden");
lasthiddenMenu = document.querySelectorAll(".last_hidden");



if (window.innerWidth >= 768) {
visibleMenu.forEach((item) => {
    item.addEventListener("mouseover", () => {
      // filter함수를 사용하여 hiddenMenu 중 key값이 item의 key값과 같은 것만 보여줌
      show = Array.from(hiddenMenu).filter((menu) => {
        return item.attributes.key.value === menu.attributes.key.value;
      });

      show.forEach((h) => {
        h.style.display = "block";
      });

      showa = Array.from(lasthiddenMenu).filter((menu) => {
        return item.attributes.key.value === menu.attributes.key.value;
      });

      showa.forEach((h) => {
        h.style.display = "block";
      });
    });
  });
  (function(){var w=window;if(w.ChannelIO){return w.console.error("ChannelIO script included twice.");}var ch=function(){ch.c(arguments);};ch.q=[];ch.c=function(args){ch.q.push(args);};w.ChannelIO=ch;function l(){if(w.ChannelIOInitialized){return;}w.ChannelIOInitialized=true;var s=document.createElement("script");s.type="text/javascript";s.async=true;s.src="https://cdn.channel.io/plugin/ch-plugin-web.js";var x=document.getElementsByTagName("script")[0];if(x.parentNode){x.parentNode.insertBefore(s,x);}}if(document.readyState==="complete"){l();}else{w.addEventListener("DOMContentLoaded",l);w.addEventListener("load",l);}})();

  ChannelIO('boot', {
    "pluginKey": "b3ffb007-1ba7-49bb-90ed-f6d0de4b9a0b"
  });

  
  visibleMenu.forEach((item) => {
    item.addEventListener("mouseout", () => {
      // filter함수를 사용하여 hiddenMenu 중 key값이 item의 key값과 같은 것만 보여줌
      show = Array.from(hiddenMenu).filter((menu) => {
        return item.attributes.key.value === menu.attributes.key.value;
      });

      show.forEach((h) => {
        h.style.display = "none";
      });

      showa = Array.from(lasthiddenMenu).filter((menu) => {
        return item.attributes.key.value === menu.attributes.key.value;
      });

      showa.forEach((h) => {
        h.style.display = "none";
      });
    });
  });

  
  hiddenMenu.forEach((item) => {
    item.addEventListener("mouseover", () => {
      show = Array.from(hiddenMenu).filter((menu) => {
        return item.attributes.key.value === menu.attributes.key.value;
      });

      show.forEach((h) => {
        h.style.display = "block";
      });

      showa = Array.from(lasthiddenMenu).filter((menu) => {
        return item.attributes.key.value === menu.attributes.key.value;
      });

      showa.forEach((h) => {
        h.style.display = "block";
      });
    });
  });
  
  hiddenMenu.forEach((item) => {
    item.addEventListener("mouseout", () => {
      show = Array.from(hiddenMenu).filter((menu) => {
        return item.attributes.key.value === menu.attributes.key.value;
      });

      show.forEach((h) => {
        h.style.display = "none";
      });

      showa = Array.from(lasthiddenMenu).filter((menu) => {
        return item.attributes.key.value === menu.attributes.key.value;
      });
      
      showa.forEach((h) => {
        h.style.display = "none";
      });
    });
  });
}







  document.addEventListener("DOMContentLoaded", () => {
    const menu = document.querySelector(".taskbar-container");
    const hamburger = document.querySelector(".hamburger");

    hamburger.addEventListener("click", () => {
        menu.classList.toggle("active");
    });

    document.addEventListener("click", (event) => {
        if (!menu.contains(event.target) && event.target !== hamburger) {
            menu.classList.remove("active");
        }
    });
});


  