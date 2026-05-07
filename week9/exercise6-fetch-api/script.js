// script.js

const btnFetch = document.getElementById('btn-fetch-posts');
const btnClear = document.getElementById('btn-clear');
const postsList = document.getElementById('posts-list');
const statusMsg = document.getElementById('status-message');
const loader = document.getElementById('loader');

// URL for the placeholder API
const API_URL = 'https://jsonplaceholder.typicode.com/posts?_limit=10';

// Function to fetch posts
async function fetchPosts() {
    // Show loader and clear existing list
    loader.classList.remove('hidden');
    postsList.innerHTML = '';
    statusMsg.innerHTML = '';

    try {
        const response = await fetch(API_URL);

        // Check if the response is successful (status 200-299)
        if (!response.ok) {
            throw new Error(`HTTP Error! Status: ${response.status}`);
        }

        const posts = await response.json();
        displayPosts(posts);
        statusMsg.innerHTML = `<p style="color: green;">Successfully loaded ${posts.length} posts.</p>`;

    } catch (error) {
        console.error("Fetch error:", error);
        statusMsg.innerHTML = `<p class="error">Failed to fetch data: ${error.message}</p>`;
    } finally {
        // Hide loader regardless of success or failure
        loader.classList.add('hidden');
    }
}

// Function to display posts in the DOM
function displayPosts(posts) {
    posts.forEach(post => {
        const li = document.createElement('li');
        li.classList.add('post-card');
        
        li.innerHTML = `
            <h3>${post.title}</h3>
            <p>${post.body}</p>
        `;
        
        postsList.appendChild(li);
    });
}

// Event Listeners
btnFetch.addEventListener('click', fetchPosts);

btnClear.addEventListener('click', () => {
    postsList.innerHTML = '';
    statusMsg.innerHTML = '';
});
