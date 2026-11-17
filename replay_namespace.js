// Read-only replay of selected configuration fields. No provider calls.
const fs = require('node:fs');
const workflow = require('./evidence/workflow_redacted.json');
const fixture = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const config = name => workflow.nodes.find(n => n.name === name).parameters;
const assigned = name => config(name).assignments.assignments.find(x => x.name === 'strategyNamespace').value;
const insert = config('Insert Custom Strategy PDF');
const read = config('Pinecone Vector Store');
const forwarded = config('Start Parallel Research').assignments.assignments.find(x => x.name === 'strategyNamespace').value;
if (!forwarded.includes('$json.strategyNamespace') || !read.options.pineconeNamespace.includes('Start Parallel Research') ||
    !read.options.pineconeNamespace.includes('.json.strategyNamespace')) throw new Error('Review changed routing');
const results = fixture.requests.map(r => ({
  studio: r.studio, upload: r.upload,
  write: r.upload ? {index: insert.pineconeIndex.value, namespace: insert.options.pineconeNamespace, clear: insert.options.clearNamespace} : null,
  read: {index: read.pineconeIndex.value, namespace: assigned(r.upload ? 'Use Custom Strategy Namespace' : 'Use Default Northstar Namespace')}
}));
const uploads = results.filter(r => r.upload);
const sameTarget = uploads.every(r => r.write.index === uploads[0].write.index && r.write.namespace === uploads[0].write.namespace && r.read.namespace === r.write.namespace);
if (!sameTarget || !uploads.some(r => r.write.clear) || results[2].read.namespace === uploads[0].read.namespace)
  throw new Error('Configuration no longer reproduces reported behavior');
console.log(JSON.stringify({results, same_custom_target: sameTarget, clear_namespace_requested: true,
  conclusion: 'In a shared hosted instance the export supplies no per-studio or per-run namespace for uploads. No real data exposure or deletion tested.'}, null, 2));
