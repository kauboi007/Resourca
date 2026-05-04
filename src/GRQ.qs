namespace mq {
    operation GRQ(): Result {
        use q = Qubit();
        H(q);
        let result = M(q);
        Reset(q);
        return result;
    }
}

//sample program to generate a random qubit - remove the above code and paste your quantum qs code
