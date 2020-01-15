'use strict';

const e = React.createElement;

class QueueBar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            queue: [
                { username: 'encryptedthoughts', section: "left", show: true },
                { username: 'decrypted', section: "left", show: false },
                { username: 'tenepe', section: "right", show: true },
                { username: 'superhappypuppy', section: "right", show: false }
            ]
        };
    }

    componentDidMount() {
        this.interval = setInterval(() => this.showNext(), 5000);
    }

    componentWillUnmount() {
        clearInterval(this.interval);
    }

    showNext() {
        var tempQueue = this.state.queue;
        for (var i = 0; i < tempQueue.length; i++) {
            if (tempQueue[i].show) {
                tempQueue[i].show = !tempQueue[i].show;
                if (i < tempQueue.length) {
                    tempQueue[i + 1].show = true;
                    this.setState({ list: tempQueue });
                    return;
                }
            }
        }

        if (tempQueue.length > 0) {
            tempQueue[0].show = !tempQueue[0].show;
            this.setState({ list: tempQueue });
        }
    }

    render() {

        var left = {};
        var right = {};

        for (var i = 0; i < this.state.queue.length; i++) {
            if (this.state.queue[i].section === "left" && this.state.queue[i].show)
                left = e('div', { className: this.state.queue[i].show ? 'fade show' : 'fade' }, this.state.queue[i].username);
        }

        for (var j = 0; j < this.state.queue.length; j++) {
            if (this.state.queue[j].section === "right" && this.state.queue[j].show)
                right = e('div', { className: this.state.queue[j].show ? 'fade show' : 'fade' }, this.state.queue[j].username);
        }

        return e('div', {},
            e('div', { className: 'd-flex flex-row justify-content-between px-2 bar' },
                left,
                right
            ),
            e('button', { onClick: () => this.setState({ show: true }) }, 'Show'),
            e('button', { onClick: () => this.setState({ show: false }) }, 'Fade'),
        );
    }
}

const domContainer = document.querySelector('#queue_container');
ReactDOM.render(e(QueueBar), domContainer);