const opener = document.querySelector(".opener")
const mainMenu = document.querySelector(".main-menu")
const closebtn = document.querySelector(".closebtn")
const opaque = document.querySelector(".opaque")

opener.addEventListener('click', () => {
        opener.classList.add("off")
        mainMenu.classList.add("opened")
        closebtn.classList.add("opened")
        opaque.classList.add("opened")
})

closebtn.addEventListener('click', () => {
    opener.classList.remove("off")
    mainMenu.classList.remove("opened")
    closebtn.classList.remove("opened")
    opaque.classList.remove("opened")
})
