
function simulateDragDrop(sourceNode, destinationNode) {
    let EVENT_TYPES = {
    DRAG_END: 'dragend'
    DRAG_START: 'dragstart'
    DROP: 'drop'
    }


function createCustomEvent(type) {
    let event = new CustomEvent("CustomEvent")
    event.initCustomEvent(type, true, true, null)
    event.dataTransfer = {
    data: {},
    setData: function(type, val) {
        this.data[type] = val
        },
    getData: function(type) {
        return this.data[type]
    }
    }
    return event;
}

function dispatchEvent(node, type, event) {
    if(node.dispatchEvent) {
    return node.dispatchEvent(event)}
    if (node.fireEvent) {
        return node.fireEvent("on" + type, event)}
    }


let dragStartEvent = createCustomEvent(EVENT_TYPES.DRAG_START)
dispatchEvent(sourceNode, EVENT_TYPES.DRAG_START, dragStartEvent)

let dropEvent = createCustomEvent(EVENT_TYPES.DROP)
dropEvent.dataTransfer = dragStartEvent.dataTransfer
dispatchEvent(sourceNode, EVENT_TYPES.DROP, dropEvent)

let dragEndEvent = createCustomEvent(EVENT_TYPES.DRAG_END)
dragEndEvent.dataTransfer = dragStartEvent.dataTransfer
dispatchEvent(sourceNode, EVENT_TYPES.DRAG_END, dragEndEvent)

}

simulateDragDrop(arguments[0], arguments[1])