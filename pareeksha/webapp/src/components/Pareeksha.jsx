import React, { Component } from 'react';
import {connect} from 'react-redux';

import {testPapers, auth} from "../actions";


class Pareeksha extends Component {

    componentDidMount() {
        this.props.fetchTestPapers();
    }

    state = {
        text: "",
        updateTestPaperId: null,
    }

    resetForm = () => {
        this.setState({text: "", updateTestPaperId: null});
    }

    selectForEdit = (id) => {
        let test_paper = this.props.test_papers[id];
        this.setState({text: test_paper.text, updateTestPaperId: id});
    }

    submitTestPaper = (e) => {
        e.preventDefault();
        if (this.state.updateTestPaperId === null) {
            this.props.addTestPaper(this.state.text).then(this.resetForm);
        } else {
            this.props.updateTestPaper(this.state.updateTestPaperId, this.state.text).then(this.resetForm);
        }
    }

    render() {
        return (
            <div>
                <h2>Welcome to Pareeksha!!!!</h2>
                <hr />
                <div style={{textAlign: "right"}}>
                    {this.props.user.email} (<a onClick={this.props.logout}>logout</a>)
                </div>

                <h3>Add new test paper</h3>
                <form onSubmit={this.submitTestPaper}>
                    <input
                        value={this.state.text}
                        placeholder="Enter desc here..."
                        onChange={(e) => this.setState({text: e.target.value})}
                        required />
                    <button onClick={this.resetForm}>Reset</button>
                    <input type="submit" value="Save Test Paper" />
                </form>

                <h3>Test Papers</h3>
                <table>
                    <tbody>
                        {this.props.test_papers.map((test_paper, id) => (
                            <tr key={`test_paper_${test_paper.id}`}>
                                <td>{test_paper.title}</td>
                                <td><button onClick={() => this.selectForEdit(id)}>edit</button></td>
                                <td><button onClick={() => this.props.deleteTestPaper(id)}>delete</button></td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        )
    }
}


const mapStateToProps = state => {
    console.log('mapping state: ');
    console.log(state);
    return {
        test_papers: state.testPapers,
        user: state.auth.user,
    }
}

const mapDispatchToProps = dispatch => {
    return {
        fetchTestPapers: () => {
            dispatch(testPapers.fetchTestPapers());
        },
        addTestPaper: (text) => {
            return dispatch(testPapers.addTestPaper(text));
        },
        updateTestPaper: (id, text) => {
            return dispatch(testPapers.updateTestPaper(id, text));
        },
        deleteTestPaper: (id) => {
            dispatch(testPapers.deleteTestPaper(id));
        },
        logout: () => dispatch(auth.logout()),
    }
}


export default connect(mapStateToProps, mapDispatchToProps)(Pareeksha);