function initMap() {
    var location = {
        lat: 42.447318,
        lng: -71.224500
    };
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
        center: location
    });

    var contentString = '<div id="content">' +
        '<div id="siteNotice">' +
        '</div>' +
        '<h5 id="firstHeading" class="firstHeading">Demo</h5>' +
        '<div id="bodyContent">' +
        '<p><b>Demo</b>, Lexington, MA 02420</p>' +
        '</div>' +
        '</div>';

    var infowindow = new google.maps.InfoWindow({
        content: contentString
    });

    var marker = new google.maps.Marker({
        position: location,
        map: map,
        title: 'Location (Lexington, MA)'
    });
    marker.addListener('click', function() {
        infowindow.open(map, marker);
    });
}