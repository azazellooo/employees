let getUpdateForm = function (e){
    e.preventDefault();
    let contentId = e.target.parentElement.id
    let targetUrl = e.target.dataset.updateurl
    let csrfToken = $( "input[name*='csrfmiddlewaretoken']" )

    console.log(csrfToken)
    console.log('xcvikjbhg')
    console.log($("#closeCreateModal"))

        $.ajax({
        url: targetUrl,
        type: 'get',
        // data: '',
        success: function(response) {
            $("#openUpdateFormModel").trigger('click')
            $("#updateModalLabel").text('Update Content')
            $("#updateForm").attr('action', targetUrl);
            $("#updateForm").attr('method', 'post');
            $("#updateForm").html(response)
            $("#updateForm").append(csrfToken)
            $("#updateForm").append(`<button type="submit" class="btn btn-success" id="${targetUrl}">update</button>`)
            $("#updateForm").append(`<!--<button type="submit" class="btn btn-success">update</button>-->`)
        },
        failure: function(response) {
            console.log(response)
            alert('ERROR');
        }
    });
}