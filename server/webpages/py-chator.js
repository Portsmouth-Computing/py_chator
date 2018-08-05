'use strict';

var initialize = function () {
    var _ref = _asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee() {
		return regeneratorRuntime.wrap(function _callee$(_context) {
			while (1) {
			    switch (_context.prev = _context.next) {
			    case 0:
			    newMsgEl.addEventListener('keydown', keyDownHandler);
			    loadMessages();

			    case 2:
			    case 'end':
			    return _context.stop();
			    }
			}
		    }, _callee, this);
	    }));

    return function initialize() {
        return _ref.apply(this, arguments);
    };
}();

var loadMessages = function () {
    var _ref2 = _asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee2() {
		var response, data;
		return regeneratorRuntime.wrap(function _callee2$(_context2) {
			while (1) {
			    switch (_context2.prev = _context2.next) {
			    case 0:
				LOADMESSAGES_RUNNING = true;
				_context2.next = 3;
				return fetch('/messages/get');

			    case 3:
				response = _context2.sent;

				if (response.ok) {
				    _context2.next = 7;
				    break;
				}

				console.error('bad response');
				return _context2.abrupt('return');

			    case 7:
				_context2.next = 9;
				return response.json();

			    case 9:
				data = _context2.sent;

				fillMessages(data);

				try {
				    setTimeout(loadMessages, AUTOREFRESH_INTERVAL);
				} catch (e) {
				    console.error(e);
				    LOADMESSAGES_RUNNING = false;
				}

			    case 12:
			    case 'end':
				return _context2.stop();
			    }
			}
		    }, _callee2, this);
	    }));

    return function loadMessages() {
        return _ref2.apply(this, arguments);
    };
}();

var addMessage = function () {
    var _ref3 = _asyncToGenerator( /*#__PURE__*/regeneratorRuntime.mark(function _callee3(e) {
		var response;
		return regeneratorRuntime.wrap(function _callee3$(_context3) {
			while (1) {
			    switch (_context3.prev = _context3.next) {
			    case 0:
				if (!(newMsgEl.value.trim() === '')) {
				    _context3.next = 3;
				    break;
				}

				newMsgEl.focus();
				return _context3.abrupt('return');

			    case 3:
				_context3.next = 5;
				return fetch('/messages/post', {
					method: 'POST',
					    body: JSON.stringify({ value: newMsgEl.value.trim() }),
					    headers: {
					    'content-type': 'application/json'
						}
				    });

			    case 5:
				response = _context3.sent;

				if (!response.ok) {
				    _context3.next = 14;
				    break;
				}

				_context3.t0 = fillMessages;
				_context3.next = 10;
				return response.json();

			    case 10:
				_context3.t1 = _context3.sent;
				(0, _context3.t0)(_context3.t1);

				newMsgEl.value = '';
				newMsgEl.focus();

			    case 14:
			    case 'end':
				return _context3.stop();
			    }
			}
		    }, _callee3, this);
	    }));

    return function addMessage(_x) {
        return _ref3.apply(this, arguments);
    };
}();

function _asyncToGenerator(fn) { return function () { var gen = fn.apply(this, arguments); return new Promise(function (resolve, reject) { function step(key, arg) { try { var info = gen[key](arg); var value = info.value; } catch (error) { reject(error); return; } if (info.done) { resolve(value); } else { return Promise.resolve(value).then(function (value) { step("next", value); }, function (err) { step("throw", err); }); } } return step("next"); }); }; }

window.addEventListener('load', initialize);
var newMsgEl = document.querySelector('#newmsg');

var AUTOREFRESH_INTERVAL = 5000; // 1s
var LOADMESSAGES_RUNNING = false;

function keyDownHandler(e) {
    if (e.defaultPrevented) {
        return; // Do nothing if the event was already processed
    }

    if (e.key === 'Enter') {
        addMessage();
        e.preventDefault();
    }
}

function fillMessages(data) {
    var ol = document.querySelector('#messages');
    ol.innerHTML = '';

    var _iteratorNormalCompletion = true;
    var _didIteratorError = false;
    var _iteratorError = undefined;

    try {
        for (var _iterator = data[Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
            var msg = _step.value;

            var li = document.createElement('li');
            li.textContent = msg.message;
            ol.appendChild(li);
        }
    } catch (err) {
        _didIteratorError = true;
        _iteratorError = err;
    } finally {
        try {
            if (!_iteratorNormalCompletion && _iterator.return) {
                _iterator.return();
            }
        } finally {
            if (_didIteratorError) {
                throw _iteratorError;
            }
        }
    }
}