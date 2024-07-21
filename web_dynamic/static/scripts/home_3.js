$(document).ready(function () {
					const userId = "{{ user_id }}";
					const username = "{{ username }}"
					$.get(`http://localhost:5001/users/projects/${userId}`, function (data, status) {

						$.each(data, function (i, obj) {

							let url = `/Echetra/${username}/${obj.name}`
							if (!obj.endDate) {
								let pid = obj.id
								pid = pid.substring(0, 3);
								$(".projects-current").append(
								`	<div class="project-current-divs">
										<div class="project-current-div1">
											<span class="project-pid">${pid}</span>
											<a href="${url}"><span class="project-div-name">${obj.name}</span></a>
											<span class="project-current-div-done">done</span>
										</div>

									</div>`);
							}
						});


						$.each(data, function (i, obj) {

							let pid2 = obj.id;
							pid2 = pid2.substring(0, 3);
							
							let container = "";

							if (obj.category === "webDevelopment") {
								container = "#weblinks";
							}
							if (obj.category === "Engineering") {
								container = "#englinks"
							}
							if (obj.category === "art") {
								container = "#artlinks"
							}


							$(`${container}`).append(
								`
								<div class="container-link">
									<span class="project-pid">${pid2}</span>
								 	<a href="/Echetra/${username}/${obj.name}">${obj.name}</a>
								</div>
								`)
						});
					});
});
					
/*function slidepCategory () {
	const webBtn = document.getElementById('category_web');
	const webContainer = document.getElementById('web-links-container');
	const webLinks = document.getElementById('weblinks');

	webBtn.addEventListener('click', () => {
						const linksHeight = webLinks.getBoundingClientRect().height;
						const containerHeight = webContainer.getBoundingClientRect().height;

						containerHeight === 0
							? webContainer.style.height = `${linksHeight}px`
							: webContainer.style.height = 0;
	});


	const engBtn = document.getElementById('category_engineering');
	const engContainer = document.getElementById('Engineering-links-container');
	const engLinks = document.getElementById('englinks');

	engBtn.addEventListener('click', () => {
	const linksHeight = engLinks.getBoundingClientRect().height;
	const containerHeight = engContainer.getBoundingClientRect().height;

						containerHeight === 0
							? engContainer.style.height = `${linksHeight}px`
							: engContainer.style.height = 0;
					});

	const artBtn = document.getElementById('category_art');
	const artContainer = document.getElementById('Art-links-container');
	const artLinks = document.getElementById('artlinks');

					artBtn.addEventListener('click', () => {
						const linksHeight = artLinks.getBoundingClientRect().height;
						const containerHeight = artContainer.getBoundingClientRect().height;

						containerHeight === 0
							? artContainer.style.height = `${linksHeight}px`
							: artContainer.style.height = 0;


					});
}

slidepCategory();
*/