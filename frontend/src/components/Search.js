import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

const Search = ({word, setWord, handleSubmit}) => {
    return (
        <>
            <Container className='mt-4' fluid="md">
                <Row className='justify-content-center'>
                    <Col xs={12} md={8} lg={6}>
                        <Form onSubmit={handleSubmit}>
                            <Row>
                                <Col xs={9}>
                                    <Form.Control
                                        type="text"
                                        value={word}
                                        id='word'
                                        onChange={(e)=> setWord(e.target.value)}
                                        placeholder="Search for new image..." 
                                    />
                                </Col>
                                <Col>
                                    <Button type="submit" variant="primary">Search</Button>
                                </Col>
                            </Row>
                        </Form>
                    </Col>
                </Row>
            </Container>
        </>
    );
}
 
export default Search;