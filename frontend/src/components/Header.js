import {Navbar, Nav, Container} from 'react-bootstrap';
import {ReactComponent as Logo} from '../images/logo.svg';

const navbarStyle={
    backgroundColor: '#eeee'
}

const Header = (props) => {
    return (
        <>
            <Navbar style={navbarStyle} data-bs-theme="light">
                <Container>
                    <Logo style={{maxWidth:"10rem", maxHeight:"2rem"}}/>
                </Container>
            </Navbar>
        </>
    );
}
 
export default Header;