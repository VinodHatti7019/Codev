// API Base URL
const API_BASE = window.location.origin;

// Load tools on page load
document.addEventListener('DOMContentLoaded', function() {
    loadTools();
    loadHistory();
});

// Execute Task
async function executeTask() {
    const taskInput = document.getElementById('taskInput');
    const toolSelect = document.getElementById('toolSelect');
    const executeBtn = document.getElementById('executeBtn');
    const resultsDiv = document.getElementById('results');

    const task = taskInput.value.trim();
    
    if (!task) {
        alert('Please enter a task');
        return;
    }

    // Disable button and show loading
    executeBtn.disabled = true;
    executeBtn.textContent = 'Executing...';
    resultsDiv.innerHTML = '<div class="placeholder"><div class="loading"></div> Processing task...</div>';

    const payload = {
        task: task,
        tool: toolSelect.value || null
    };

    try {
        const response = await fetch(`${API_BASE}/api/execute`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        const result = await response.json();

        if (response.ok) {
            displayResult(result);
            loadHistory(); // Refresh history
            taskInput.value = ''; // Clear input
        } else {
            resultsDiv.innerHTML = `<div class="result-card"><span class="status failed">Error</span><p>${result.error}</p></div>`;
        }
    } catch (error) {
        resultsDiv.innerHTML = `<div class="result-card"><span class="status failed">Error</span><p>Failed to execute task: ${error.message}</p></div>`;
    } finally {
        executeBtn.disabled = false;
        executeBtn.textContent = 'Execute Task';
    }
}

// Display Result
function displayResult(result) {
    const resultsDiv = document.getElementById('results');
    
    let resultHTML = `
        <div class="result-card">
            <h3>Task #${result.task_id}</h3>
            <span class="status ${result.status}">${result.status.toUpperCase()}</span>
            <p><strong>Task:</strong> ${result.task}</p>
            <p><strong>Tool Used:</strong> ${result.tool_used}</p>
            <p><strong>Duration:</strong> ${result.duration.toFixed(2)}s</p>
    `;

    if (result.status === 'completed' && result.result) {
        resultHTML += '<div class="result-content"><h4>Result:</h4>';
        
        const data = result.result;
        
        if (data.code) {
            resultHTML += `<p><strong>Language:</strong> ${data.language}</p>`;
            resultHTML += `<p><strong>Type:</strong> ${data.code_type}</p>`;
            resultHTML += `<pre><code>${escapeHtml(data.code)}</code></pre>`;
        } else if (data.documentation) {
            resultHTML += `<pre><code>${escapeHtml(data.documentation)}</code></pre>`;
        } else if (data.results) {
            resultHTML += `<p><strong>Found ${data.num_results} results:</strong></p><ul>`;
            data.results.forEach(item => {
                resultHTML += `<li>${escapeHtml(item)}</li>`;
            });
            resultHTML += '</ul>';
        } else {
            resultHTML += `<pre><code>${JSON.stringify(data, null, 2)}</code></pre>`;
        }
        
        resultHTML += '</div>';
    } else if (result.error) {
        resultHTML += `<p><strong>Error:</strong> ${result.error}</p>`;
    }

    resultHTML += '</div>';
    resultsDiv.innerHTML = resultHTML;
}

// Load Tools
async function loadTools() {
    const toolsDiv = document.getElementById('tools');
    const toolSelect = document.getElementById('toolSelect');

    try {
        const response = await fetch(`${API_BASE}/api/tools`);
        const data = await response.json();

        if (data.tools && data.tools.length > 0) {
            // Update tools display
            toolsDiv.innerHTML = '';
            data.tools.forEach(tool => {
                const toolCard = document.createElement('div');
                toolCard.className = 'tool-card';
                toolCard.innerHTML = `
                    <h3>${tool.name}</h3>
                    <p>${tool.description}</p>
                `;
                toolsDiv.appendChild(toolCard);
            });

            // Update tool select dropdown
            data.tools.forEach(tool => {
                const option = document.createElement('option');
                option.value = tool.name;
                option.textContent = tool.name;
                toolSelect.appendChild(option);
            });
        } else {
            toolsDiv.innerHTML = '<p class="placeholder">No tools available</p>';
        }
    } catch (error) {
        toolsDiv.innerHTML = '<p class="placeholder">Failed to load tools</p>';
    }
}

// Load History
async function loadHistory() {
    const historyDiv = document.getElementById('history');

    try {
        const response = await fetch(`${API_BASE}/api/history`);
        const data = await response.json();

        if (data.history && data.history.length > 0) {
            historyDiv.innerHTML = '';
            // Show most recent first
            data.history.reverse().forEach(task => {
                const historyItem = document.createElement('div');
                historyItem.className = 'history-item';
                historyItem.innerHTML = `
                    <div class="task-id">Task #${task.task_id}</div>
                    <div class="task-text">${escapeHtml(task.task)}</div>
                    <div class="task-meta">
                        <span class="status ${task.status}">${task.status}</span>
                        | Tool: ${task.tool_used}
                        | Duration: ${task.duration.toFixed(2)}s
                    </div>
                `;
                historyDiv.appendChild(historyItem);
            });
        } else {
            historyDiv.innerHTML = '<p class="placeholder">No tasks executed yet.</p>';
        }
    } catch (error) {
        historyDiv.innerHTML = '<p class="placeholder">Failed to load history</p>';
    }
}

// Helper function to escape HTML
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Allow Enter key to execute task (with Shift+Enter for new line)
document.getElementById('taskInput').addEventListener('keydown', function(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        executeTask();
    }
});
