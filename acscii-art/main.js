const figlet = require('figlet');
const prompts = require('prompts');

const pattern = /^[abc]*[0-9]*$\S/i

let generate = async function() {
    let processor = await prompts({
        type: 'text',
        name: 'input',
        message: 'Input a string',
        validate: input => test(pattern, input) ? 'String may only contain letters and numbers' : true
    });

    console.log(processor.input);
}

generate();