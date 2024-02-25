document.oncontextmenu = new Function("return false");
let waitLock = null;

if ("wakeLock" in navigator) {
    try {
        waitLock =  await navigator.waitLock.request('screen');
        console.log("wakeLock acquired");
        logMsg = "wakeLock acquired";
    } catch (error) {
        console.log(error, "wakeLock not acquired");
        logMsg = String(error);
    }
}

let logMsg = "";

export default {
    data() {
        return {
            message: logMsg
        }
    },
    methods: {
        clickButton(id) {
            navigator.vibrate(100);
            let domain = window.location.origin.split(":")[1];
            console.log(domain);
            fetch(`http://${domain}:8000/api/v1/key/${id}`)
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                })
                .catch(error => {
                    console.log(error);
                });
        }
    }
};