import ReactDOM from 'react-dom';
import { act } from 'react-dom/test-utils';
import ErrorMessage from './ErrorMessage';

let container: HTMLDivElement;

beforeEach(() => {
  container = document.createElement('div');
  document.body.appendChild(container);
});

afterEach(() => {
  document.body.removeChild(container);
});


it('can render and text is passed in', () => {
    // Test first render and componentDidMount
    act(() => {
        ReactDOM.render(<ErrorMessage>test error message</ErrorMessage>, container);
    });
    const message = container.getElementsByClassName('error-message')[0];
    expect(message.textContent).toBe('test error message');
});
