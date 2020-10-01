
/**
 * functions related to IFrame
 */
const frameRender = {

    /**
     * настраиваемая функция для отправки сообщения из IFrame в родительский 
     */
    passControlsMessage: function () { },

    /**
     * функция для привязки событий изменения элементов к отправке сообщений
     */
    bindEvents: function () {
        let passMsg = this.passControlsMessage.bind(this);
        let divElement = document.querySelector('body');

        // все элементы ввода
        let inputElements = divElement.querySelectorAll('input');
        for (let elem of inputElements) {

            // устанавливает значение метки для ползунка диапазона
            let setRangeLabelValue = function() {
                if (elem.type == "range") {
                    // находит элемент метки рядом с ползунком
                    let next = elem.nextElementSibling;
                    next.innerHTML = elem.value;
                }
            };

            setRangeLabelValue();

            elem.oninput = function () {
                setRangeLabelValue();
                passMsg();
            }
        }
    },// bindEvents

    /**
     * custom function to call when received data from the main window 
     */
    receiveData: function (data) {

    }
} // frameRender

/**
 * To pass message to parent window
 */
window.onload = function () {
    frameRender.bindEvents();
    frameRender.passControlsMessage();
};

/**
 * To receive message from parent window
 */
window.addEventListener(
    "message",
    function (e) {
      var key = e.message ? "message" : "data";
      var data = e[key];
      frameRender.receiveData(data);
    },
    false
  );


