/*jshint esversion: 6 */
/* globals $ */

$(document).ready(function () {
    console.log('Hello')
    // Source: Boutique Ado walkthrough project
    // Script for sorting functionality
    $('#sort-selector').change(function () {
        var selector = $(this);
        var currentUrl = new URL(window.location);

        var selectedVal = selector.val();
        if (selectedVal != "reset") {
            var sort = selectedVal.split("_")[0];
            var direction = selectedVal.split("_")[1];

            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");

            window.location.replace(currentUrl);
        }
    });
    // $('#sort-selector span').click(function () {
    //     var selector = $(this);
    //     var currentUrl = new URL(window.location);
    
    //     var selectedVal = selector.attr("value");
    //     if (selectedVal != "reset") {
    //         var sort = selectedVal.split("_")[0];
    //         var direction = selectedVal.split("_")[1];
    
    //         currentUrl.searchParams.set("sort", sort);
    //         currentUrl.searchParams.set("direction", direction);
    
    //         window.location.replace(currentUrl);
    //     } else {
    //         currentUrl.searchParams.delete("sort");
    //         currentUrl.searchParams.delete("direction");
    
    //         window.location.replace(currentUrl);
    //     }
    // });
    
});

// $('#sort-selector span').click(function () {
//     var selector = $(this);
//     var selectedVal = selector.attr("value");
//     var sort = "";
//     var direction = "";

//     if (selectedVal != "reset") {
//         sort = selectedVal.split("_")[0];
//         direction = selectedVal.split("_")[1];
//     }

//     $.ajax({
//         url: window.location.pathname, // Use the current URL path
//         type: 'GET',
//         data: {
//             sort: sort,
//             direction: direction,
//             q: getQueryParameter('q') // Include the search query if present
//         },
//         success: function(data) {
//             $('#product-list').html(data);
//             window.history.pushState({}, '', updateURLParameter(window.location.href, 'sort', sort));
//             window.history.pushState({}, '', updateURLParameter(window.location.href, 'direction', direction));
//         },
//         error: function(xhr, status, error) {
//             console.error('AJAX Error: ' + status + error);
//         }
//     });
// });

// function getQueryParameter(name) {
//     const urlParams = new URLSearchParams(window.location.search);
//     return urlParams.get(name);
// }

// function updateURLParameter(url, param, paramVal) {
//     var newAdditionalURL = "";
//     var tempArray = url.split("?");
//     var baseURL = tempArray[0];
//     var additionalURL = tempArray[1];
//     var temp = "";

//     if (additionalURL) {
//         tempArray = additionalURL.split("&");
//         for (var i = 0; i < tempArray.length; i++) {
//             if (tempArray[i].split('=')[0] != param) {
//                 newAdditionalURL += temp + tempArray[i];
//                 temp = "&";
//             }
//         }
//     }

//     var rows_txt = temp + "" + param + "=" + paramVal;
//     return baseURL + "?" + newAdditionalURL + rows_txt;
// }
