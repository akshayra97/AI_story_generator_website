const B2 = require('backblaze-b2');

const b2 = new B2({
    accountId: 'yourAccountId',
    applicationKey: 'yourApplicationKey'
});

async function listBuckets() {
    await b2.authorize();  // Authorize with the provided credentials
    const response = await b2.listBuckets();
    console.log(response.data);  // Log the list of buckets
}

listBuckets();
