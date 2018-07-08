const initialState = [];

export default function testPapers(state=initialState, action) {
    let testPaperList = state.slice();

    switch (action.type) {

        case 'FETCH_TEST_PAPERS':
            console.log([...state, ...action.test_papers]);
            return [...state, ...action.test_papers];

        case 'ADD_TEST_PAPER':
            return [...state, action.test_paper];

        case 'UPDATE_TEST_PAPER':
            let testPaperToUpdate = testPaperList[action.index];
            testPaperToUpdate.text = action.test_paper.text;
            testPaperList.splice(action.index, 1, testPaperToUpdate);
            return testPaperList;

        case 'DELETE_TEST_PAPER':
            testPaperList.splice(action.index, 1);
            return testPaperList;

        default:
            return state;
    }
};