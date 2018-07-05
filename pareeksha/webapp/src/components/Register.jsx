import React, {Component} from "react";
import {connect} from "react-redux";

import {Link, Redirect} from "react-router-dom";

import {auth} from "../actions";

class Register extends Component {

    state = {
        email: "",
        password: "",
        first_name: "",
        last_name: "",
        role: ""
    }

    onSubmit = e => {
        e.preventDefault();
        this.props.register(
            this.state.email,
            this.state.password,
            this.state.first_name,
            this.state.last_name,
            this.state.role,
        );
    }

    render() {
        if (this.props.isAuthenticated) {
            return <Redirect to="/" />
        }
        return (
            <form onSubmit={this.onSubmit}>
                <fieldset>
                    <legend>Register</legend>
                    {this.props.errors.length > 0 && (
                        <ul>
                            {this.props.errors.map(error => (
                                <li key={error.field}>{error.message}</li>
                            ))}
                        </ul>
                    )}
                    <p>
                        <label htmlFor="email">email</label>
                        <input
                            type="text" id="email"
                            onChange={e => this.setState({email: e.target.value})} />
                    </p>
                    <p>
                        <label htmlFor="password">Password</label>
                        <input
                            type="password" id="password"
                            onChange={e => this.setState({password: e.target.value})} />
                    </p>
                    <p>
                        <label htmlFor="first_name">First Name</label>
                        <input
                            type="text" id="first_name"
                            onChange={e => this.setState({first_name: e.target.value})} />
                    </p>
                    <p>
                        <label htmlFor="last_name">Last Name</label>
                        <input
                            type="text" id="last_name"
                            onChange={e => this.setState({last_name: e.target.value})} />
                    </p>
                    <p>
                        <label htmlFor="role">Role</label>
                        <input
                            type="text" id="role"
                            onChange={e => this.setState({role: e.target.value})} />
                    </p>
                    <p>
                        <button type="submit">Register</button>
                    </p>

                    <p>
                        Already have an account? <Link to="/login">Login</Link>
                    </p>
                </fieldset>
            </form>
        )
    }
}

const mapStateToProps = state => {
    let errors = [];
    if (state.auth.errors) {
        errors = Object.keys(state.auth.errors).map(field => {
            return {field, message: state.auth.errors[field]};
        });
    }
    return {
        errors,
        isAuthenticated: state.auth.isAuthenticated
    };
}

const mapDispatchToProps = dispatch => {
    return {
        register: (
            email, 
            password, 
            first_name, 
            last_name, 
            role) => dispatch(auth.register(email, password, first_name, last_name, role)),
    };
}

export default connect(mapStateToProps, mapDispatchToProps)(Register);