document.addEventListener('DOMContentLoaded', () => {
    console.log("js works")
    document.addEventListener("click", event => {
        let element = event.target;
        console.log(element.className)
        if (element.className == "btn btn-outline-danger") {
            let grandparent = element.parentElement.parentElement;

            let el = grandparent.querySelector(".selectpicker");
            console.log(el.className);
            console.log(el);
            var cnt = 0;
            for (var i = 0; i < el.options.length; i++) {
                if (el.options[i].selected) {
                    console.log(el.options[i]);
                    cnt++;
                }
            }
            console.log(cnt);
            var allowed = el.getAttribute("data-max-options");
            console.log(allowed)
            if (allowed != null) {
                allowed = Number(allowed);
                console.log(typeof allowed);
                console.log(typeof cnt);
                if (cnt != allowed) {
                    event.preventDefault();
                    alert(`You have to choose ${allowed} toppings`)
                }
            }

        }




    })
})
