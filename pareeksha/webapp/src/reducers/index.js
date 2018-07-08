import { combineReducers } from 'redux';
import auth from "./auth";
import testPapers from "./testPapers";


const pareeksha = combineReducers({
    auth,
    testPapers,
})

export default pareeksha;